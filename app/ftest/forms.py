from django import forms
from ftest.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', )
