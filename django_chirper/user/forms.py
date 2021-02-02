from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, EmailInput, PasswordInput
from django.forms.fields import CharField, EmailField


class RegistrationForm(UserCreationForm):
    input_field_class = 'bg-gray-700 bg-opacity-0 ml-2 mt-2 outline-none text-white'

    username = CharField(
        max_length = 50, 
        label = 'Name',
        widget = TextInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    email = EmailField(
        label = 'Email', 
        widget = EmailInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    password1 = CharField(
        max_length = 250,
        label = 'Password',
        widget = PasswordInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    password2 = CharField(
        max_length = 250, 
        label = 'Confirm Password',
        widget = PasswordInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
    input_field_class = 'ml-2 h-10 bg-gray-700 bg-opacity-0 outline-none text-white'

    username = CharField(
        max_length = 50,
        label = 'Phone, email, or username',
        widget = TextInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    password = CharField(
        max_length = 250,
        label = 'Password',
        widget = PasswordInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    # non_field_errors = ('''
    #     There was unusual login activity on your account. 
    #     To help keep your account safe, please enter your phone number 
    #     or email address to verify it’s you.
    # ''')

    class Meta: 
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)