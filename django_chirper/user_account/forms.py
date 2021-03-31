from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.forms.fields import CharField, EmailField, BooleanField
from django.forms.widgets import EmailInput, PasswordInput, CheckboxInput
from django.contrib.auth.models import User


class BeginPasswordResetForm(PasswordResetForm):
    email = EmailField(
        label = 'Email',
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


class ResetPasswordForm(SetPasswordForm):
    input_field_class = 'border border-gray-400 rounded-full focus:border-blue-500 focus:outline-none w-88 h-10 pl-3'

    new_password1 = CharField(
        label = 'New password',
        widget = PasswordInput(
            attrs = {
                'autocomplete': 'new-password',
                'class': input_field_class
            }
        ),
        strip = False,
        help_text = password_validation.password_validators_help_text_html(),
    )

    new_password2 = CharField(
        label = 'New password confirmation',
        strip = False,
        widget = PasswordInput(
            attrs = {
                'autocomplete': 'new-password',
                'class': input_field_class
            }
        ),
    )

    remember = BooleanField(
        label = 'Remember me',
        widget = CheckboxInput(
            attrs = {
                'checked': 'checked',
                'class': 'form-checkbox'
            }
        )
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)