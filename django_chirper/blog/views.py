from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return HttpResponse('<h1>About Page</h1>')