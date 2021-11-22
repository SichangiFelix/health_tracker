from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import user

from .models import Order

class CreateUserForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['username', 'email', 'password1', 'password2']