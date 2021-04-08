from django.forms import ModelForm
from django.forms.widgets import Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': Textarea(attrs = {
                'rows': 6, 
                'placeholder': "What's happening?",
                'class': 'resize-none bg-gray-900 text-xl focus:outline-none p-2'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# same as PostForm, only difference at placeholder
class PostReplyForm(PostForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': Textarea(attrs = {
                'rows': 6, 
                'placeholder': "Chirp your reply",
                'class': 'resize-none bg-gray-900 text-xl focus:outline-none p-2'
            })
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)