from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from user.models import Profile
from message.models import Message


@login_required
def messages(request):
    request.user.profile.last_checked_message_at = timezone.now()
    request.user.profile.save()

    following_profiles = request.user.profile.following.all()
    context = {
        'following_profiles': following_profiles
    }
    return render(request, 'messages.html', context = context)


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


@login_required
def messages_compose(request):
    following_profiles = request.user.profile.following.all()
    context = {
        'following_profiles': following_profiles
    }
    return render(request, 'messages_compose.html', context)