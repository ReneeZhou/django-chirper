from django.urls import path
from . import views


urlpatterns = [
    path('compose/chirp/', views.compose_chirp, name = 'compose_chirp')
]