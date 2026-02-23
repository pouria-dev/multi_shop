""" Develop specific forms

 forms:

    -Login and register user
    -Dashboard user admin

 """
from importlib.metadata import requires

from django import forms
from django.contrib.auth import get_user_model 
from django.forms import ValidationError


get_user_model() # return user model that we have created inmodels.py
User = get_user_model() # assign user model to User variable


class Login_Form(forms.Form):
    email = forms.CharField(max_length=120 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'Password'}))


