from django.shortcuts import render, redirect
from blog.models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    if request.user.is_authenticated:
        return render(request, 'home.html', context)
    else: 
        return render(request, 'home_notauth.html')