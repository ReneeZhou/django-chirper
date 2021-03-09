from django.db.models.expressions import OuterRef
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q, When, Case
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from user.models import Profile
from message.models import Message
from message.forms import MessageForm


class BaseMessageView(LoginRequiredMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['following_profiles'] = self.request.user.profile.following.all()
        return context


class MessageView(BaseMessageView):
    template_name = 'messages.html'

    # update timestamp everytime user check msg page, need to cascade down to messages/.../
    def get_queryset(self):
        self.request.user.profile.last_checked_message_at = timezone.now()
        self.request.user.save()
        return 


@login_required
def messages_counterpart(request, counterpart_id, currentuser_id):
    counterpart = Profile.objects.get(id = counterpart_id)

    if counterpart is None: 
        return redirect('messages')
    else: 
        following_profiles = request.user.profile.following.all()
        form = MessageForm(request.POST or None)

        msg_f = Message.objects.filter(sender_id = counterpart_id, recipient_id = currentuser_id)
        msg_t = Message.objects.filter(sender_id = currentuser_id, recipient_id = counterpart_id)
        message_history = (msg_t | msg_f).order_by('created_at') 

        context = {
            'counterpart': counterpart,
            'following_profiles': following_profiles,
            'message_history': message_history,
            'form': form
        }

        if form.is_valid():
            form.instance.sender_id = currentuser_id
            form.instance.recipient_id = counterpart_id
            form.save()
            return redirect('messages_counterpart', counterpart_id = counterpart.id, currentuser_id = request.user.profile.id)

    return render(request, 'messages_counterpart.html', context)


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