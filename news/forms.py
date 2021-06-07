from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announce', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название статьи',
                'class': 'form-control',
            }),
            'announce': TextInput(attrs={
                'placeholder': 'Анонс статьи',
                'class': 'form-control',
            }),
            'full_text': Textarea(attrs={
                 'placeholder': 'Текст статьи',
                 'class': 'form-control',
            }),
            'date': DateTimeInput(attrs={
                 'class': 'form-control',
            }),
        }
