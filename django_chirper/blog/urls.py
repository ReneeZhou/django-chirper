from django.urls import path
from .views import StatusDetailView, StatusCreateView, StatusUpdateView, StatusDeleteView


urlpatterns = [
    path('<str:handle>/status/<int:pk>/', StatusDetailView.as_view(), name = 'status'),
    path('<str:handle>/status/<int:pk>/update/', StatusUpdateView.as_view(), name = 'update_chirp'),
    path('compose/chirp/', StatusCreateView.as_view(), name = 'compose_chirp'),
]