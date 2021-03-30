from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.widgets import EmailInput
from django.contrib.auth.models import User


class BeginPasswordResetForm(PasswordResetForm):
    email = EmailField(
        label = 'Email' ,
        max_length = 254,
        widget = EmailInput(
            attrs = {
                'autocomplete': 'email',
                'class': 'border border-gray-400 rounded-full focus:border-blue-500 focus:outline-none w-88 h-10 pl-3'
            }
        )
    )
    def clean_email(self):
        data = self.cleaned_data['email']
        if not User.objects.filter(email = data).all():
            raise ValidationError("We couldn't find your account with that information.")
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)