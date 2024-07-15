from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'live_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başlık'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'İçerik'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'live_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'title': 'Başlık',
            'content': 'İçerik',
            'image': 'Fotoğraf',
            'live_date': 'Yayınlanma Tarihi',
        }
