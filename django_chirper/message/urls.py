from django.urls import path
from . import views
from .views import MessageView, MessageComposeView, MessageCounterpartView, MessageCounterpartInfoView


urlpatterns = [
    path('messages/', MessageView.as_view(), name = 'messages'),
    path(
        'messages/<int:counterpart_id>-<int:currentuser_id>/',
        MessageCounterpartView.as_view(),
        name = 'messages_counterpart'
    ),
    path(
        'messages/<int:counterpart_id>-<int:currentuser_id>/info/', 
        MessageCounterpartInfoView.as_view(), 
        name = 'messages_counterpart_info'
    ),
    path('messages/compose/', MessageComposeView.as_view(), name = 'messages_compose'),
    path('messages/<int:pk>/like_message/', views.like_message, name = 'like_message'),
    path('messages/<int:pk>/unlike_message/', views.unlike_message, name = 'unlike_message')
]