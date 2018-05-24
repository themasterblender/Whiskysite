from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 

class CreateUserForm(ModelForm):
    class Meta:
        model = UserCreationForm
        fields = '__all__'
