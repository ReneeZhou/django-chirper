from django.forms import ModelForm
from django.forms.fields import CharField
from django.forms.widgets import Textarea
from .models import Post


class PostForm(ModelForm):
    content = CharField(
        widget = Textarea(
            attrs = {
                'maxlength': 280, 
                'rows': 6,
                'placeholder': 'What\'s happening?',
                'class': 'resize-none bg-gray-900 text-xl focus:outline-none p-2' 
            }
        )
    )


    class Meta:
        model = Post
        fields = ['content', 'created_at', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)