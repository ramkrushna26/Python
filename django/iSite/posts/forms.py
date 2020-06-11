from django import forms 
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ['title', 'author_description', 'image', 'content']