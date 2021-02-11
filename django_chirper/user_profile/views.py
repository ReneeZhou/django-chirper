from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.defaults import page_not_found
from user.models import Profile
from blog.models import Post


class ProfilePostView(ListView):
    template_name = 'profile.html'

    def get_queryset(self):
        self.user_profile = get_object_or_404(Profile, handle = self.kwargs['handle'])    # from the url
        return Post.objects.filter(id = self.user_profile.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.user_profile
        return context


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
            return render(request, 'profile_media.html', context)
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