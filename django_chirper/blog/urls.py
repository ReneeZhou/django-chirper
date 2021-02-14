from django.urls import path
from . import views
from .views import StatusDetailView


urlpatterns = [
    path('<str:handle>/status/<int:pk>/', StatusDetailView.as_view(), name = 'status'),
    path('compose/chirp/', views.compose_chirp, name = 'compose_chirp')
]