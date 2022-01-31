"""
Form based on the PenpalProfile model
"""

from django import forms

from .models import PenpalProfile


class PenpalForm(forms.ModelForm):
    """
    Form to create a new penpal profile
    based on the PenpalProfile model
    """

    class Meta:
        """
        Excludes the user field from the form.
        Read-only field imported from User model.
        """

        model = PenpalProfile
        exclude = [
            'user'
        ]
