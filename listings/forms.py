"""
Module containing forms for listing-related functionality.
"""
from django import forms
from django_countries.fields import CountryField
from .models import House



class HouseForm(forms.ModelForm):
    """Form for creating listings or houses """
    country = CountryField().formfield()
    class Meta:
        """classes for creating listings or houses """
        model = House
        fields = ['title', 'description', 'price','image','contact', 'address', 'status','country']
        