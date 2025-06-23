from django import forms 
from .models import Speak
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Speakforms(forms.ModelForm):
    class Meta:
        model= Speak
        fields = ['text','photo']

class user_Regs_form(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        