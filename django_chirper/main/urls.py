from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('explore/', views.explore, name = 'explore'),
    path('notifications/', views.notifications, name = 'notifications'),
    path('notifications/mentions/', views.notifications_mentions, name = 'notifications_mentions'),
    path('messages/', views.messages, name = 'messages'),
    path('messages/compose/', views.messages_compose, name = 'messages_compose'),
    path('bookmarks/', views.bookmarks, name = 'bookmarks'),
    path('lists/create/', views.lists_create, name = 'lists_create'),
    path('lists/add_member/', views.lists_addMember, name = 'lists_addMember'),
    path('i/trends/', views.trends, name = 'trends'),
    path('i/timeline/', views.timeline, name = 'timeline'),
    path('i/connect_people', views.connectPeople, name = 'connectPeople')
]