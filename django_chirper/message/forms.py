from django.forms.models import ModelForm
from django.forms.widgets import Textarea
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('body', )
        widgets = {
            'body': Textarea(
                attrs = {
                    'placeholder': 'Start a new message',
                    'max_length': 600,
                    'rows': 1,
                    'class': 
                        '''
                        resize-none outline-none bg-gray-700 bg-opacity-25 focus:bg-gray-900 
                        rounded-full px-3 pr-10 py-1 text-tiny placeholder-gray-600 border 
                        border-transparent focus-within:border-blue-500 w-116
                        '''
                }
            )
        }