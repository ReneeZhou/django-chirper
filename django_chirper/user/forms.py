from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.fields import CharField, EmailField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML
from crispy_forms.layout import Field as CrispyField
from django.forms.widgets import TextInput


class UserRegisterForm(UserCreationForm):
    input_field_class = 'bg-gray-700 bg-opacity-0 ml-2 mt-2 outline-none text-white'

    username = CharField(
        max_length = 50, 
        label = 'Name',
        widget = forms.TextInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    email = EmailField(
        label = 'Email', 
        widget = forms.EmailInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    password1 = CharField(
        max_length = 250,
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    password2 = CharField(
        max_length = 250, 
        label = 'Confirm Password',
        widget = forms.PasswordInput(
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


class UserLoginForm(AuthenticationForm):
    input_field_class = 'ml-2 h-10 bg-gray-700 bg-opacity-0 outline-none text-white'

    username = CharField(
        max_length = 50,
        label = 'Phone, email, or username',
        widget = forms.TextInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    password = CharField(
        max_length = 250,
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {
                'class': input_field_class
            }
        )
    )

    non_field_errors = ('''
        There was unusual login activity on your account. 
        To help keep your account safe, please enter your phone number 
        or email address to verify it’s you.
    ''')

    class Meta: 
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class VUserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('username').label = 'Phone, email, or username'
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            CrispyField(
                Div(
                    'username',
                    'password',
                    css_class = 'space-y-5 w-128'
                ),
            ),
            Submit('submit', 'Log in', \
                css_class = 'rounded-full bg-blue-500 hover:bg-blue-600 active:bg-blue-700 w-128 h-12 \
                font-bold outline-none cursor-pointer text-white mt-5'),
        )


class HUserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('username').label = 'Phone, email, or username'
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            CrispyField(
                Div(
                    Div(
                    Div('username', css_class = 'w-56'),
                    Div(
                        'password', 
                        HTML('''
                            <a href="" 
                            class="text-blue-500 text-xs ml-2 no-underline hover:underline">
                            Forgot password?</a>
                        '''),
                        css_class = 'flex flex-col w-56'
                    ),
                    css_class = 'flex flex-row w-108 h-24 space-x-4 ml-4 mt-4 text-gray-600 text-base'
                ),
                Submit('submit', 'Log in', 
                    css_class = 'text-blue-500 text-base font-semibold bg-gray-900 cursor-pointer \
                        border border-blue-500 rounded-full whitespace-no-wrap h-10 w-20 ml-4 mt-6 px-3 py-2 \
                            hover:bg-gray-800 hover:bg-opacity-50 focus:outline-none focus:bg-gray-700'),
                css_class = 'flex flex-row'
                )
                
            ),
            
        )