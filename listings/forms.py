from django import forms
from .models import House
from django_countries.fields import CountryField


class HouseForm(forms.ModelForm):
    country = CountryField().formfield()
    
    class Meta:
        model = House
        fields = ['title', 'description', 'price','image','contact', 'address', 'status','country']