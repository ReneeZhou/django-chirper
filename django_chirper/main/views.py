from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog.models import Post
from .forms import PostForm


@login_required
def home(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        posts = Post.objects.filter(
            Q(author = request.user.profile) |
            Q(author__in = request.user.profile.following.all())
        ).order_by('-created_at')
        context = {
            'posts': posts,
            'form': form
        }
        if form.is_valid():
            form.instance.author = request.user.profile
            form.save()
            return redirect('home')
        return render(request, 'home.html', context)
        
    else: 
        return redirect('home_notauth')


def explore(request):
    context = {
        'topics': topics,
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
def bookmarks(request):
    return render(request, 'bookmarks.html')


@login_required
def lists_create(request):
    return render(request, 'lists_create.html')


@login_required
def lists_addMember(request):
    return render(request, 'lists_addMember.html')


# i, explore/
@login_required
def trends(request):
    return render(request, 'trends.html', {'topics': topics})


# i, explore/
@login_required
def timeline(request):
    return render(request, 'timeline.html', {'happenings': happenings})


# i
@login_required
def connectPeople(request):
    return render(request, 'connectPeople.html')


# i, dp
@login_required
def followerRequests(request):
    return render(request, 'followerRequests.html')


# i, dp 
@login_required
def display(request):
    return render(request, 'display.html')


# i, dp
def keyboardShortcuts(request):
    return render(request, 'keyboardShortcuts.html')



topics = [
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