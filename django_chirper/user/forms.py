from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, EmailInput, PasswordInput
from django.forms.fields import CharField, EmailField


class RegistrationForm(UserCreationForm):
    class Meta:
        input_field_class = 'bg-gray-700 bg-opacity-0 ml-2 mt-2 outline-none text-white'
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Name',
            'email': 'Email',
        }
        widgets = {
            'username': TextInput(
                attrs = {
                    'class': input_field_class
                }
            ),
            'email': TextInput(
                attrs = {
                    'class': input_field_class
                }
            )
        },
        #  to change username max_length
        #  will need custom User model
        #  current max_length = 150
        #  unless generate field using Form instead of ModelForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

        self.fields['password1'].widget = PasswordInput(attrs = {'class': 'bg-gray-700 bg-opacity-0 ml-2 mt-2 outline-none text-white'})
        self.fields['password2'].widget = PasswordInput(attrs = {'class': 'bg-gray-700 bg-opacity-0 ml-2 mt-2 outline-none text-white'})
        # Username is an actual field on User model, overriding Meta works
        # Password1 & Password2 are fields defined only in form
        # therefore, overriding Meta would not work


class LoginForm(AuthenticationForm):
    input_field_class = 'ml-2 h-10 bg-gray-700 bg-opacity-0 outline-none text-white'

    username = CharField(
        label = 'Phone, email, or username',
        widget = TextInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    password = CharField(
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
    
    # no class Meta here as AuthenticationForm is not a ModelForm