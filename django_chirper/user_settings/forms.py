from django.forms import ModelForm
from django.forms.fields import CharField, ImageField, URLField
from django.forms.widgets import TextInput, Textarea, URLInput, FileInput
from django.contrib.auth.models import User
from user.models import Profile


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