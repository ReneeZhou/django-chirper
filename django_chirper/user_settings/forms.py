from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from django.forms.fields import CharField, ImageField, URLField
from django.forms.widgets import TextInput, Textarea, URLInput, FileInput, PasswordInput
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
        widget = Textarea(
            attrs = {
                'class': input_field_class + ' resize-none',
                'placeholder': 'Add your bio',
                'rows': 3
            }
        )
    )

    location = CharField(
        widget = TextInput(
            attrs = {
                'class': input_field_class,
                'placeholder': 'Add your location'
            }
        )
    )

    website = URLField(
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