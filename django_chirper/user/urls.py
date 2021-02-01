from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home_notauth, name = 'home_notauth'),
    path('signup/', views.signup, name = 'signup'),
]