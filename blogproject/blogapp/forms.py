from django import forms
from .models import Blogs


class BlogPostForm(forms.ModelForm):
    class Meta():
        model = Blogs
        fields = ['title','text']