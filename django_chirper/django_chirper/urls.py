"""django_chirper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user.forms import VUserLoginForm, HUserLoginForm
# from user import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/', user_views.signup, name = 'signup'),
    # class based views
    path('login/',
        auth_views.LoginView.as_view(
            template_name = 'login.html', 
            authentication_form = VUserLoginForm
            ), 
        name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('', auth_views.LoginView.as_view(
        template_name = 'home_notauth.html', 
        authentication_form = HUserLoginForm),
        name = 'home_notauth'),
    path('', include('main.urls')),
    path('', include('user.urls')),
    path('', include('user_profile.urls'))
]