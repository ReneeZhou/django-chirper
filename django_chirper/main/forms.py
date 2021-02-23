from django.forms import ModelForm
from django.forms.widgets import TextInput
from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', )
        widgets = {
            'content': TextInput(attrs = {
                'placeholder': "What's happening?",
                'rows': 1,
                'class': 'resize-none bg-gray-900 text-xl focus:outline-none p-2'
            })
        }
