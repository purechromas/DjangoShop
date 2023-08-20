from django import forms

from blogs.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug', 'is_published', 'view_count')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Title'
            }),
            'contained': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 6, 'placeholder': 'Contained'
            }),
            'preview_image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'title': '',
            'contained': '',
            'preview_image': '',
        }
