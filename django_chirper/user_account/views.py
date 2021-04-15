from django.shortcuts import redirect
from django.urls import reverse_lazy
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

    def get(self, request, *args, **kwargs):
        if self.request.META.get('HTTP_REFERER') is None:
            return redirect('account_beginPasswordReset')
        else: 
            return super().get(request, *args, **kwargs)


class ResetPasswordView(PasswordResetConfirmView):
    template_name = 'account_resetPassword.html'
    form_class = ResetPasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account'] = User.objects.get(email = self.request.session['email'])
        context['context'] = context.items()
        return context


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'account_resetPasswordComplete.html'

    def get(self, request, *args, **kwargs):
        if self.request.META.get('HTTP_REFERER') is None:
            return redirect('account_beginPasswordReset')
        else: 
            return super().get(request, *args, **kwargs)