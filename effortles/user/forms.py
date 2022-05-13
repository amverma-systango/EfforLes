from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"