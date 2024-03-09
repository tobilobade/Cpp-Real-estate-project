from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(validators=[validators.validate_email])
    first_name = forms.CharField()
    last_name = forms.CharField()
    
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class Meta:
    model = User
    fields = ['username', 'first_name','last_name','email', 'password1', 'password2']