from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
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


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Post                                                # model still needed even if 
    form_class = PostForm                                       # form_class is ModelForm
    template_name = 'compose_chirp.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'compose_chirp.html'

    def test_func(self):
        return self.request.user.profile.handle == self.kwargs['handle']


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    http_method_names = ['post']
    model = Post

    def get_success_url(self):
        return reverse('profile', kwargs = {'handle': self.kwargs['handle']})