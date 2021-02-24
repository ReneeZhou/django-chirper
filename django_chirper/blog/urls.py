from django.urls import path
from .views import StatusDetailView, StatusCreateView


urlpatterns = [
    path('<str:handle>/status/<int:pk>/', StatusDetailView.as_view(), name = 'status'),
    path('compose/chirp/', StatusCreateView.as_view(), name = 'compose_chirp'),
]