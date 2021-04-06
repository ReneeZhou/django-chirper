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
    # path(
    #     'messages/<int:counterpart_id>-<int:currentuser_id>/', 
    #     views.messages_counterpart, 
    #     name = 'messages_counterpart'
    # ),
    path(
        'messages/<int:counterpart_id>-<int:currentuser_id>/info/', 
        MessageCounterpartInfoView.as_view(), 
        name = 'messages_counterpart_info'
    ),
    path('messages/compose/', MessageComposeView.as_view(), name = 'messages_compose')
]