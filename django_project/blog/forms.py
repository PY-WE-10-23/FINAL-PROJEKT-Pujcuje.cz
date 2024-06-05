from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Item, Post, Image


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'content']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'price','content','image','category','author']

"""
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image")
"""
"""
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []
"""