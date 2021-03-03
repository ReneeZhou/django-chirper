from django.urls import path
from .views import (
    StatusDetailView, StatusCreateView, StatusUpdateView, StatusDeleteView,
    like_chirp, unlike_chirp
)


urlpatterns = [
    path('<str:handle>/status/<int:pk>/', StatusDetailView.as_view(), name = 'status'),
    path('<str:handle>/status/<int:pk>/update/', StatusUpdateView.as_view(), name = 'update_chirp'),
    path('<str:handle>/status/<int:pk>/delete/', StatusDeleteView.as_view(), name = 'delete_chirp'),
    path('<str:handle>/status/<int:pk>/like_chirp/', like_chirp, name = 'like_chirp'),
    path('<str:handle>/status/<int:pk>/unlike_chirp/', unlike_chirp, name = 'unlike_chirp'),
    path('compose/chirp/', StatusCreateView.as_view(), name = 'compose_chirp'),
]