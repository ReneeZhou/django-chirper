from django.urls import path
from . import views
from .views import MessagesView


urlpatterns = [
    path('messages/', MessagesView.as_view(), name = 'messages'),
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