from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView)
from .forms import BeginPasswordResetForm


class BeginPasswordResetView(FormView):
    template_name = 'account_beginPasswordReset.html'
    form_class = BeginPasswordResetForm
    success_url = reverse_lazy('account_sendPasswordReset')


class SendPasswordResetView(PasswordResetView):
    template_name = 'account_sendPasswordReset.html'