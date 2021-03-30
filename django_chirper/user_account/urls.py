from django.urls import path
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView)
from .views import (BeginPasswordResetView, SendPasswordResetView)


urlpatterns = [
    path('begin_password_reset/', BeginPasswordResetView.as_view(), name = 'account_beginPasswordReset'),
    path('send_password_reset/', SendPasswordResetView.as_view(), name = 'account_sendPasswordReset'),
]