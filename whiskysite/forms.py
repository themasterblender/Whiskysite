#from django.forms import ModelForm
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 

# 16/06/2018 Nuova classe per registrarenuovi utenti con conferma trmaite email
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# 16/06/2018 Vecchia classe per la registrazione di nuovi utenti senza conferma email
#class CreateUserForm(ModelForm):
#    class Meta:
#        model = UserCreationForm
#        fields = '__all__'
