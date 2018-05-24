from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 

from .models import Category
    
class CreateCollectionForm(forms.Form):
    #Definisco i campi necessari per registrare una nuova collezione
    #(owner, created_date e published_date saranno impostati automaticamente
    title = forms.CharField(max_length=40, label='Collection name')
    text = forms.CharField(required=False, label='Describe your collection')
    #Definisco i campi necessari per registrare una nuova bottiglia
    whisky_type = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    name = forms.CharField(max_length=40)
    distillery = forms.CharField(max_length=40, required=False)
    bottler = forms.CharField(max_length=40)
    age = forms.IntegerField(required=False)
    year_bottled = forms.DecimalField(max_digits=4, decimal_places=0, required=False)
    purchased_date = forms.DateField()
    purchased_place = forms.CharField(max_length=40, required=False)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    bottle_code = forms.CharField(max_length = 20, required=False)

class CreateBottleForm(forms.Form):
    #Definisco i campi necessari per registrare una nuova bottiglia
    whisky_type = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    name = forms.CharField(max_length=40)
    distillery = forms.CharField(max_length=40, required=False)
    bottler = forms.CharField(max_length=40)
    age = forms.IntegerField(required=False)
    year_bottled = forms.DecimalField(max_digits=4, decimal_places=0, required=False)
    purchased_date = forms.DateField()
    purchased_place = forms.CharField(max_length=40, required=False)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    bottle_code = forms.CharField(max_length = 20, required=False)

