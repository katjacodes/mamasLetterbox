from django import forms
from django_countries.fields import CountryField
from .models import PenpalProfile


class PenpalForm(forms.ModelForm):
    class Meta:
        model = PenpalProfile
        fields = "__all__"
