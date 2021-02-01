from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.fields import CharField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML
from crispy_forms.layout import Field as CrispyField


class UserRegisterForm(UserCreationForm):
    username = CharField(max_length = 50, label = 'Name')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'email': 'Email',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('password2').label = 'Confirm Password'
        self.fields.get('password1').help_text = None
        self.fields.get('password2').help_text = None

        self.helper = FormHelper()
        self.helper.layout = Layout(
            CrispyField(
                Div(
                    'username', 
                    'email', 
                    HTML('''
                        <p class="text-blue-600 text-sm font-medium no-underline hover:underline cursor-pointer pb-4">User phone instead</p>
                        '''),
                    'password1',
                    'password2',
                    css_class = 'space-y-5'
                ),
            ),
            Submit('submit', 'Sign Up', css_class = 'bg-blue-500 rounded-full h-12 w-128 font-bold outline-none \
                hover:bg-blue-600 cursor-pointer mt-6 self-center text-white'),
        )


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