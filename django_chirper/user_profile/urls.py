from django.urls import path
from . import views


urlpatterns = [
    path('<str:handle>/', views.profile, name = 'profile')
]