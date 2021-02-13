from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
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


class ProfileRepliesView(ProfilePostView):
    template_name = 'profile_withReplies.html'


class ProfileMediaView(ProfilePostView):
    template_name = 'profile_media.html'


class ProfileLikesView(ProfilePostView):
    template_name = 'profile_likes.html'