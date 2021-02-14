from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from user.models import Profile
from .forms import PostForm
from .models import Post


class StatusDetailView(DetailView):
    template_name = 'status.html'

    def get_queryset(self):
        self.user_profile = get_object_or_404(Profile, handle = self.kwargs['handle'])
        self.post = get_object_or_404(Post, id = self.kwargs['pk'])
        return Post.objects.filter(id = self.post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post
        context['user_profile'] = self.user_profile
        return context


@login_required
def compose_chirp(request):
    form = PostForm()
    return render(request, 'compose_chirp.html', {'form': form})