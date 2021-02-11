from django.urls import path
from . import views
from .views import ProfilePostView


urlpatterns = [
    path('<str:handle>/', ProfilePostView.as_view(), name = 'profile'),
    path('<str:handle>/with_replies/', views.profile_withReplies, name = 'profile_withReplies'),
    path('<str:handle>/media/', views.profile_media, name = 'profile_media'), 
    path('<str:handle>/likes', views.profile_likes, name = 'profile_likes')
]