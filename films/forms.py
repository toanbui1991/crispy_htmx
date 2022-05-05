from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_htmx.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]