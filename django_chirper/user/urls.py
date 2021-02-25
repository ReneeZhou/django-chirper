from django.contrib.auth.models import User
from django.urls import path
from . import views
from .views import UserCreateView

urlpatterns = [
    path('', views.home_notauth, name = 'home_notauth'),
    path('signup/', UserCreateView.as_view(), name = 'signup')
]