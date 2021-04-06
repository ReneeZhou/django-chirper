from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import Profile
from message.models import Message
from message.forms import MessageForm


class BaseMessageView(LoginRequiredMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        history_counterparts = Message.objects.raw(
            '''
            WITH last_msg AS (
                SELECT *
                    FROM
                    (
                    SELECT id, sender_id as counterpart, body, created_at
                    FROM message_message
                    WHERE recipient_id = %s
                    UNION
                    SELECT id, recipient_id as counterpart, body, created_at
                    FROM message_message
                    WHERE sender_id = %s
                    ) 
                GROUP BY counterpart
                HAVING created_at = Max(created_at)
            )

            SELECT user_profile.id, auth_user.username, user_profile.handle, user_profile.profile_image,
                last_msg.created_at, last_msg.body 
            FROM last_msg
            LEFT JOIN user_profile
            ON last_msg.counterpart = user_profile.id
            LEFT JOIN auth_user
            ON auth_user.id = user_profile.user_id;
            ''',
            [self.request.user.profile.id, self.request.user.profile.id]
        )

        context['history_counterparts'] = history_counterparts
        context['following_profiles'] = self.request.user.profile.following.all()
        return context


class MessageView(BaseMessageView):
    template_name = 'messages.html'

    # update timestamp everytime user check msg page, need to cascade down to messages/.../
    def get_queryset(self):
        self.request.user.profile.last_checked_message_at = timezone.now()
        self.request.user.save()
        return 


class MessageCounterpartView(FormView, BaseMessageView):
    model = Message
    template_name = 'messages_counterpart.html'
    form_class = MessageForm

    def get_queryset(self):
        self.counterpart_id = self.kwargs['counterpart_id']
        self.currentuser_id = self.kwargs['currentuser_id']
        return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counterpart'] = Profile.objects.get(id = self.counterpart_id)
        msg_f = Message.objects.filter(sender_id = self.counterpart_id, recipient_id = self.currentuser_id)
        msg_t = Message.objects.filter(sender_id = self.currentuser_id, recipient_id = self.counterpart_id)
        message_history = (msg_t | msg_f).order_by('created_at') 
        context['message_history'] = message_history
        return context

    def form_valid(self, form):
        self.counterpart_id = self.kwargs['counterpart_id']
        self.currentuser_id = self.kwargs['currentuser_id']
        form.instance.recipient_id = self.counterpart_id
        form.instance.sender_id = self.currentuser_id
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'messages_counterpart',
            kwargs = {
                'counterpart_id': self.counterpart_id,
                'currentuser_id': self.currentuser_id
            }
        )


class MessageCounterpartInfoView(BaseMessageView):
    template_name = 'messages_counterpart_info.html'
    
    def get_queryset(self):
        self.counterpart_id = self.kwargs['counterpart_id']
        return 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counterpart'] = Profile.objects.get(id = self.counterpart_id)
        return context
        

class MessageComposeView(BaseMessageView):
    template_name = 'messages_compose.html'

    def get_queryset(self):
        self.following_profiles = self.request.user.profile.following.all()
        return self.following_profiles