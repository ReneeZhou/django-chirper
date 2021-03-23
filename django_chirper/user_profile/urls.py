from django.urls import path
from . import views
from .views import (ProfilePostView, ProfileRepliesView, ProfileMediaView, ProfileLikesView,
    ProfileFollowersView, ProfileFollowingView, ProfileFollowersYouKnowView, ProfileSuggestedView,
    ProfileListsView, ProfileTopicsView, ProfileMomentsView)


urlpatterns = [
    path('', ProfilePostView.as_view(), name = 'profile'),
    path('with_replies/', ProfileRepliesView.as_view(), name = 'profile_withReplies'),
    path('media/', ProfileMediaView.as_view(), name = 'profile_media'), 
    path('likes/', ProfileLikesView.as_view(), name = 'profile_likes'),
    path('followers/', ProfileFollowersView.as_view(), name = 'profile_followers'),
    path('following/', ProfileFollowingView.as_view(), name = 'profile_following'),
    path('followers_you_know/', ProfileFollowersYouKnowView.as_view(), name = 'profile_followersYouKnow'),
    path('suggested/', ProfileSuggestedView.as_view(), name = 'profile_suggested'),
    path('lists/', ProfileListsView.as_view(), name = 'profile_lists'),
    path('topics/', ProfileTopicsView.as_view(), name = 'profile_topics'),
    path('moments/', ProfileMomentsView.as_view(), name = 'profile_moments'),
    path('follow/', views.follow, name = 'follow'),
    path('unfollow/', views.unfollow, name = 'unfollow')
]