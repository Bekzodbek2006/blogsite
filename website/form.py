from dataclasses import fields
from django.contrib.auth.views import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *
from django.contrib.auth.views import LoginView
User = get_user_model()

class ContactUs(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = (
            'Name',
            'Email',
            'Subject',
            'YourMassage',
        )

class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

class AddChart(forms.ModelForm):
    class Meta:
        model = Chart
        fields = (
            'country',
            'visits',
        )