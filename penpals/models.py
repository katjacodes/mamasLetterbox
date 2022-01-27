from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from .choices import Language

"""
A penpal profile model for maintainining
searchable information to match penpals
"""

class PenpalProfile(models.Model):
    language1 = models.CharField(
        max_length=10,
        choices=Language.choices,
        default=Language.ENG,
        null=False,
        blank=False,
    )
    language2 = models.CharField(
        max_length=10,
        choices=Language.choices,
        default=Language.ENG,
        blank=True,
        null=True,
    )
    language3 = models.CharField(
        max_length=10, 
        choices=Language.choices, 
        default=Language.ENG, 
        blank=True, 
        null=True
    )
    
    name = models.CharField(max_length=50, null=False, blank=False, default="Your name")
    pronoun = models.CharField(max_length=50, null=False, blank=False, default="Your preferred pronoun/s)")
    age = models.IntegerField(blank=True, null=True)
    country = CountryField(null=False, blank=False)
    hobby1 = models.CharField(max_length=50, null=False, blank=False, default="Something you enjoy")
    hobby2 = models.CharField(max_length=50, blank=True, null=True)
    hobby3 = models.CharField(max_length=50, blank=True, null=True)
    childAge1 = models.IntegerField(null=False, blank=False, default=0)
    childAge2 = models.IntegerField(blank=True, null=True)
    childAge3 = models.IntegerField(blank=True, null=True)
    childAge4 = models.IntegerField(blank=True, null=True)
    childAge5 = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=50, null=False, blank=False, default="Your email address")

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='penpal')


    def __str__(self):
        return f'{self.name}'
