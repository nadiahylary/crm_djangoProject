from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Your Email"}))
    name = forms.CharField(label="Your Complete Name", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Your Complete Name"}))
