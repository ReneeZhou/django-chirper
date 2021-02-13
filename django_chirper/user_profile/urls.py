from django.urls import path
from . import views
from .views import ProfilePostView, ProfileRepliesView, ProfileMediaView, ProfileLikesView


urlpatterns = [
    path('<str:handle>/', ProfilePostView.as_view(), name = 'profile'),
    path('<str:handle>/with_replies/', ProfileRepliesView.as_view(), name = 'profile_withReplies'),
    path('<str:handle>/media/', ProfileMediaView.as_view(), name = 'profile_media'), 
    path('<str:handle>/likes', ProfileLikesView.as_view(), name = 'profile_likes')
]