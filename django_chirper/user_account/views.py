from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView)
from .forms import BeginPasswordResetForm, ResetPasswordForm
from django.contrib.auth.models import User


class BeginPasswordResetView(PasswordResetView):
    template_name = 'account_beginPasswordReset.html'
    form_class = BeginPasswordResetForm
    success_url = reverse_lazy('account_confirmPasswordReset')
    
    # added user search to session, show result next page
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.request.session['email'] = form.cleaned_data['email']
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ConfirmPasswordResetView(PasswordResetDoneView):
    template_name = 'account_confirmPasswordReset.html'


class ResetPasswordView(PasswordResetConfirmView):
    template_name = 'account_resetPassword.html'
    form_class = ResetPasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = User.objects.get(email = self.request.session['email'])
        context['context'] = context.items()
        return context