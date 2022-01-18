from django import forms
from .models import PenpalProfile


class PenpalProfileForm(forms.ModelForm):
    class Meta:
        model = PenpalProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'age': 'Age',
            'pronoun': 'Pronouns',
            'country': 'Country',
            'hobby1': 'First Hobby',
            'hobby2': 'Second Hobby',
            'hobby3': 'Third Hobby',
            'childAge1': 'Age First Child',
            'childAge2': 'Age Second Child',
            'childAge3': 'Age Third Child',
            'childAge4': 'Age Fourth Child',
            'childAge5': 'Age Fifth Child'
        }
        
        self.fields['pronoun'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False
