from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User


User = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',  'profile_image', 'password1', 'password2']
