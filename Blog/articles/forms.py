from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'announcement_post', 'text', 'category', 'status']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'announcement_post': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'category': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
            'status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус статьи',
                'value': '0'
            }),
        }

