from django.forms import ModelForm, Form
from django.forms.fields import BooleanField, CharField, ImageField, URLField
from django.forms.widgets import CheckboxInput, EmailInput, Select, TextInput, Textarea, URLInput, FileInput, PasswordInput
from django.contrib.auth.models import User
from user.models import Profile


class SettingsAuthForm(Form):
    input_field_class = 'ml-2 bg-gray-800 bg-opacity-0 text-lg text-white outline-none'
    password = CharField(
        label = 'Password',
        widget = PasswordInput(
            attrs = {
                'class': input_field_class,
            }
        ),
    )


class UpdateScreenNameForm(ModelForm):
    handle = CharField(
            label = 'Username',
            widget = TextInput(
                attrs = {
                    'class': 'ml-2 bg-gray-800 bg-opacity-0 text-lg text-white outline-none'
                }
            )
    )
    class Meta:
        model = Profile
        fields = ('handle', )


class UpdatePhoneForm(ModelForm):
    class Meta:
        input_field_class = '''flex flex-col bg-gray-700 bg-opacity-25 border-b-2 border-gray-600
                    focus-within:border-blue-500 focus-within:text-blue-500'''
        model = Profile
        fields = ('country_code', 'phone', 'phone_public')
        labels = {
            'phone': 'Your phone number'
        }
        widgets = {
            'country_code': Select(
                attrs = {
                    'class': '''form-select border-transparent text-xl 
                            bg-gray-700 bg-opacity-0 outline-none text-white cursor-pointer'''
                }
            ),
            'phone': TextInput(
                attrs = {
                    'class': 'text-xl bg-gray-700 bg-opacity-0 ml-2 mt-2 outline-none text-white'
                }
            ),
            'phone_public': CheckboxInput(
                attrs = {
                    'checked': 'checked',
                    'class': '''form-checkbox bg-transparent border-2 border-gray-600 
                            text-xl cursor-pointer'''
                }
            )

        }


class UpdateEmailForm(ModelForm):
    email_public = BooleanField(
        widget = CheckboxInput(
            attrs = {
                'checked': 'checked',
                'class': '''form-checkbox bg-transparent border-2 border-gray-600 
                    text-xl cursor-pointer'''
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', )
        widgets = {
            'email': EmailInput(
                attrs = {
                    'class': 'text-xl bg-gray-700 bg-opacity-0 ml-2 mt-2 outline-none text-white'
                }
            )
        }


class UpdateUsernameForm(ModelForm):
    username = CharField(
        max_length = 50, 
        label = 'Name',
        widget = TextInput(
            attrs = {
                'placeholder': 'Add your name',
                'class': 'bg-gray-700 bg-opacity-0 ml-2 pb-1 outline-none text-white placeholder-gray-600'
            }
        )
    )

    class Meta: 
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class UpdateProfileForm(ModelForm):
    input_field_class = 'bg-gray-700 bg-opacity-0 ml-2 pb-1 outline-none text-white placeholder-gray-600'

    profile_image = ImageField(
        label = '',
        widget = FileInput(
            attrs = {
                'class': 'hidden',
                'accept': '.jpg,.png'
            }
        )
    )

    background_image = ImageField(
        widget = FileInput(
            attrs = {
                'class': 'hidden',
                'accept': '.jpg,.png'
            }
        )
    )

    bio = CharField(
        required = False,
        widget = Textarea(
            attrs = {
                'class': input_field_class + ' resize-none',
                'placeholder': 'Add your bio',
                'rows': 3
            }
        )
    )

    location = CharField(
        required = False,
        widget = TextInput(
            attrs = {
                'class': input_field_class,
                'placeholder': 'Add your location'
            }
        )
    )

    website = URLField(
        required = False,
        max_length = 100,
        widget = URLInput(
            attrs = {
                'class': input_field_class,
                'placeholder': 'Add your website'
            }
        )
    )

    class Meta: 
        model = Profile
        fields = [
            'profile_image',
            'background_image',
            'bio',
            'location',
            'website'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)