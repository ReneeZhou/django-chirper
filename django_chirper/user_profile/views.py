from django.shortcuts import render
from django.views.defaults import page_not_found
from user.models import Profile


def profile(request, handle):
    try: 
        user_profile = Profile.objects.get(handle = handle)
        if user_profile:
            context = {
                'user': user_profile.user
            }
            return render(request, 'profile.html', context)
    except Profile.DoesNotExist:
        return page_not_found(request, None, 'errors/404.html')