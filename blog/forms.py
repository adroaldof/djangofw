from django import forms

from .models import Category, Blog


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['slug',]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['slug',]
