from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('explore/', views.explore, name = 'explore'),
    path('notifications/', views.notifications, name = 'notifications'),
    path('notifications/mentions/', views.notifications_mentions, name = 'notifications_mentions')
]