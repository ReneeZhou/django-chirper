from django.urls import path
from . import views


urlpatterns = [
    path('messages/', views.messages, name = 'messages'),
    path(
        'messages/<int:counterpart_id>-<int:currentuser_id>/', 
        views.messages_counterpart, 
        name = 'messages_counterpart'
    ),
    path(
        'messages/<int:counterpart_id>-<int:currentuser_id>/info/', 
        views.messages_counterpart_info, 
        name = 'messages_counterpart_info'
    ),
    path('messages/compose/', views.messages_compose, name = 'messages_compose')
]