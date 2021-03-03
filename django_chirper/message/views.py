from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def messages(request):
    request.user.profile.last_checked_message_at = timezone.now()
    request.user.profile.save()
    return render(request, 'messages.html')
