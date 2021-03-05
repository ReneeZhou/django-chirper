from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


from user.models import Profile
from message.models import Message


class MessageView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messages.html'

    # update timestamp everytime user check msg page, need to cascade down to messages/.../
    def get_queryset(self):
        self.request.user.profile.last_checked_message_at = timezone.now()
        self.request.user.save()
        return 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['following_profiles'] = self.request.user.profile.following.all()
        return context


@login_required
def messages_counterpart(request, counterpart_id, currentuser_id):
    counterpart = Profile.objects.get(id = counterpart_id)

    if counterpart is None: 
        return redirect('messages')
    else: 
        following_profiles = request.user.profile.following.all()
        
        msg_f = Message.objects.filter(sender_id = counterpart_id, recipient_id = currentuser_id)
        msg_t = Message.objects.filter(sender_id = currentuser_id, recipient_id = counterpart_id)
        message_history = (msg_t | msg_f).order_by('created_at') 

        context = {
            'counterpart': counterpart,
            'following_profiles': following_profiles,
            'message_history': message_history
        }

    return render(request, 'messages_counterpart.html', context)


@login_required
def messages_counterpart_info(request, counterpart_id, currentuser_id):
    counterpart = Profile.objects.get(id = counterpart_id)

    if counterpart is None: 
        return redirect('messages')
    else: 
        following_profiles = request.user.profile.following.all()
        context = {
            'counterpart': counterpart,
            'following_profiles': following_profiles
        }

    return render(request, 'messages_counterpart_info.html', context)


class MessageComposeView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'messages_compose.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['following_profiles'] = self.request.user.profile.following.all()
        return context