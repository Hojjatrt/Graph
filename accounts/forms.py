from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from accounts.models import *
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': True}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('stu_num',)
        widgets = {
            'stu_num': forms.TextInput(attrs={'type': 'number',
                                              'min': 911000000,
                                              'max': 982000000,
                                              'placeholder': 941100000}),
        }
