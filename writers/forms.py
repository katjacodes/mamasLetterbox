from django import forms
from django_countries.fields import CountryField
from .models import WriterProfile


class WriterProfileForm(forms.ModelForm):
    class Meta:
        model = WriterProfile
        fields = ['default_username', 'default_first_name', 'default_last_name', 'age', 'pronoun',
                  'country', 'language1', 'language2', 'language3', 'hobby1',
                  'hobby2', 'hobby3', 'childAge1', 'childAge2', 'childAge3',
                  'childAge4', 'childAge4', 'childAge5']

        pronoun = forms.CharField(max_length=50, label="Pronoun/s (Required)")
        age = forms.IntegerField(label="Age")
        country = CountryField().formfield(label="Country (Required)")
        hobby1 = forms.CharField(max_length=50, label="First Hobby (Required)")
        hobby2 = forms.CharField(max_length=50, label="Second Hobby")
        hobby3 = forms.CharField(max_length=50, label="Third Hobby")
        childAge1 = forms.IntegerField(label="Age First Child (Required)")
        childAge2 = forms.IntegerField(label="Age Second Child")
        childAge3 = forms.IntegerField(label="Age Third Child")
        childAge4 = forms.IntegerField(label="Age Fourth Child")
        childAge5 = forms.IntegerField(label="Age Fifth Child")
