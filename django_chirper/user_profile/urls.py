from django.urls import path
from . import views
from .views import (ProfilePostView, ProfileRepliesView, ProfileMediaView, ProfileLikesView,
    ProfileFollowersView, ProfileFollowingView, ProfileFollowersYouKnowView, ProfileSuggestedView)


urlpatterns = [
    path('', ProfilePostView.as_view(), name = 'profile'),
    path('with_replies/', ProfileRepliesView.as_view(), name = 'profile_withReplies'),
    path('media/', ProfileMediaView.as_view(), name = 'profile_media'), 
    path('likes/', ProfileLikesView.as_view(), name = 'profile_likes'),
    path('followers/', ProfileFollowersView.as_view(), name = 'profile_followers'),
    path('followers/', ProfileFollowingView.as_view(), name = 'profile_following'),
    path('followers/', ProfileFollowersYouKnowView.as_view(), name = 'profile_followersYouKnow'),
    path('followers/', ProfileSuggestedView.as_view(), name = 'profile_suggested'),
    path('follow/', views.follow, name = 'follow'),
    path('unfollow/', views.unfollow, name = 'unfollow')
]