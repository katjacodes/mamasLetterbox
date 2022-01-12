from django import forms
from django_countries.fields import CountryField
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
