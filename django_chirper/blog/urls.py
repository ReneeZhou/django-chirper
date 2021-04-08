from django.urls import path
from .views import (
    StatusDetailView, StatusCreateView, StatusUpdateView, StatusDeleteView,
    like_chirp, unlike_chirp, 
    StatusReplyView, StatusAnalyticsView
)
from .forms import PostReplyForm


urlpatterns = [
    path('<str:handle>/status/<int:pk>/', StatusDetailView.as_view(), name = 'status'),
    path('<str:handle>/status/<int:pk>/update/', StatusUpdateView.as_view(), name = 'update_chirp'),
    path('<str:handle>/status/<int:pk>/delete/', StatusDeleteView.as_view(), name = 'delete_chirp'),
    path('<str:handle>/status/<int:pk>/like_chirp/', like_chirp, name = 'like_chirp'),
    path('<str:handle>/status/<int:pk>/unlike_chirp/', unlike_chirp, name = 'unlike_chirp'),
    path('<str:handle>/status/<int:pk>/analytics/', StatusAnalyticsView.as_view(), name = 'status_analytics'),
    path('compose/chirp/', StatusCreateView.as_view(), name = 'compose_chirp'),
    path('compose/reply/<int:pk>/', StatusReplyView.as_view(), name = 'compose_reply')
]