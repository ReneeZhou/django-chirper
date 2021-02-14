from django.urls import path
from . import views
from .views import ProfilePostView, ProfileRepliesView, ProfileMediaView, ProfileLikesView


urlpatterns = [
    path('', ProfilePostView.as_view(), name = 'profile'),
    path('with_replies/', ProfileRepliesView.as_view(), name = 'profile_withReplies'),
    path('media/', ProfileMediaView.as_view(), name = 'profile_media'), 
    path('likes', ProfileLikesView.as_view(), name = 'profile_likes')
]