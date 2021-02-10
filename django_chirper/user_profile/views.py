from django.shortcuts import render
from django.views.defaults import page_not_found
from user.models import Profile


def profile(request, handle):
    try: 
        user_profile = Profile.objects.get(handle = handle)
        if user_profile:
            context = {
                'user_profile': user_profile
            }
            return render(request, 'profile.html', context)
    except Profile.DoesNotExist:
        return page_not_found(request, None, 'errors/404.html')


def profile_withReplies(request, handle):
    try: 
        user_profile = Profile.objects.get(handle = handle)
        if user_profile:
            context = {
                'user_profile': user_profile
            }
            return render(request, 'profile_withReplies.html', context)
    except Profile.DoesNotExist:
        return page_not_found(request, None, 'errors/404.html')


def profile_media(request, handle):
    try: 
        user_profile = Profile.objects.get(handle = handle)
        if user_profile:
            context = {
                'user_profile': user_profile
            }
            return render(request, 'profile_likes.html', context)
    except Profile.DoesNotExist:
        return page_not_found(request, None, 'errors/404.html')


def profile_likes(request, handle):
    try: 
        user_profile = Profile.objects.get(handle = handle)
        if user_profile:
            context = {
                'user_profile': user_profile
            }
            return render(request, 'profile_likes.html', context)
    except Profile.DoesNotExist:
        return page_not_found(request, None, 'errors/404.html')