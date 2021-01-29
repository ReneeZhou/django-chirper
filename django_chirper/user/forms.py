from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
            Div(
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
        )
    