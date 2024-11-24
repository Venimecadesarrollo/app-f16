from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput(attrs={"placeholder": "Enter your username", "class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password", "class": "form-control"}),
    )
