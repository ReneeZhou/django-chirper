from django.urls import path
from . import views


urlpatterns = [
    path('<str:handle>/', views.profile, name = 'profile'),
    path('<str:handle>/with_replies/', views.profile_withReplies, name = 'profile_withReplies'),
    path('<str:handle>/media/', views.profile_media, name = 'profile_media'), 
    path('<str:handle>/likes', views.profile_likes, name = 'profile_likes')
]