# -*- coding: utf-8 -*-
from django import forms
from libraryapp.models import Bookdata
from libraryapp.models import login_users
from libraryapp.models import make_query
class Userform(forms.Form):  
    username = forms.CharField(label = 'Username:')  
    password = forms.CharField(label = 'Password:',widget = forms.PasswordInput())
    email = forms.EmailField(label = 'Email_ID:')  
    mobile = forms.IntegerField("Mobile_No:")  

class LoginForm(forms.Form):  
    username = forms.CharField(max_length=50)  
    Password = forms.CharField(max_length=50)

class Queryform(forms.ModelForm):  
    class Meta:  
        model = make_query
        fields = "__all__" 