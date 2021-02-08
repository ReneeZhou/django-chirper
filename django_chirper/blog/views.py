from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm


@login_required
def compose_chirp(request):
    form = PostForm()
    return render(request, 'compose_chirp.html', {'form': form})