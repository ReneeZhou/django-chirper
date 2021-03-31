from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView)
from .forms import BeginPasswordResetForm, SendPasswordResetForm


class BeginPasswordResetView(FormView):
    template_name = 'account_beginPasswordReset.html'
    form_class = BeginPasswordResetForm
    success_url = reverse_lazy('account_sendPasswordReset')

    # added user search to session, show result next page
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.request.session['email'] = form.cleaned_data['email']
            return self.form_valid(form)
        else:
            return self.form_invalid(form)