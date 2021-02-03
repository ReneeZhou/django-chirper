from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    if request.user.is_authenticated:
        return render(request, 'home.html', context)
    else: 
        return redirect('home_notauth')


def explore(request):
    context = {
        'trends': trends,
        'happenings': happenings
        }
    return render(request, 'explore.html', context)


@login_required
def notifications(request):
    return render(request, 'notifications.html')


@login_required
def notifications_mentions(request):
    return render(request, 'notifications_mentions.html')


@login_required
def messages(request):
    return render(request, 'messages.html')


@login_required
def messages_compose(request):
    return render(request, 'messages_compose.html')


trends = [
    {
        'label': 'label 1',
        'topic': 'topic 1',
        'content': 'content 1',
        'chirp_count': 'count 1'
    },
    {
        'label': 'label 2',
        'topic': 'topic 2',
        'content': 'content 2',
        'chirp_count': 'count 2'
    }
]

happenings = [
    {
        'label': 'label 1',
        'time': 'time 1',
        'title': 'title 1'
    },
    {
        'label': 'label 2',
        'time': 'time 2',
        'title': 'title 2'
    }
]

people = [
    {   
        'icon': 'icon 1',
        'username': 'username 1',
        'handle': '@handle 1'
    },
    {
        'icon': 'icon 2',
        'username': 'username 2',
        'handle': '@handle 2'
    }
]