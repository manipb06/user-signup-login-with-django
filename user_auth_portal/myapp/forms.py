from dataclasses import field, fields
import email
import pwd
from django import forms
from django.contrib.auth.models import User


class myform(forms.Form):
    first_name= forms.CharField(max_length=256)
    last_name= forms.CharField(max_length=256)
    username= forms.CharField(max_length=256)
    email= forms.EmailField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_pass = forms.CharField(widget=forms.PasswordInput())
    
    class meta():
        model = User
        fields = ('first_name','last_name','username','email','password')