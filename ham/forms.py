from django import forms
from .models import Ham
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class HamForm(forms.ModelForm):
    class Meta:
        model = Ham
        fields = ['text', 'photo']
        
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    