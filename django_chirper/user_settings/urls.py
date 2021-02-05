from django.urls import path
from . import views


urlpatterns = [
    path('settings/profile/', views.settings_profile, name = 'settings_profile')
]