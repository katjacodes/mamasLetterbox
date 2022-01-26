from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from .choices import Language

# Create your models here.

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
    language3 = models.CharField(max_length=10, choices=Language.choices, default=Language.ENG, blank=True, null=True)
    name = models.CharField(max_length=50, null=False, blank=False, help_text="Your name")
    pronoun = models.CharField(max_length=50, null=False, blank=False, help_text="Your preferred pronoun/s)")
    age = models.IntegerField(blank=False, help_text="Your age")
    country = CountryField(null=False, blank=False)
    hobby1 = models.CharField(max_length=50, null=False, blank=False, help_text="A hobby")
    hobby2 = models.CharField(max_length=50, blank=True, null=True, help_text="Second hobby (optional)")
    hobby3 = models.CharField(max_length=50, blank=True, null=True, help_text="Third hobby (optional)")
    childAge1 = models.IntegerField(null=False, blank=False)
    childAge2 = models.IntegerField(blank=True, null=True, help_text="Second child's age (optional)")
    childAge3 = models.IntegerField(blank=True, null=True, help_text="Third child's age (optional)")
    childAge4 = models.IntegerField(blank=True, null=True, help_text="Fourth child's age (optional)")
    childAge5 = models.IntegerField(blank=True, null=True, help_text="Fifth child's age (optional)")
    email = models.EmailField(max_length=50, null=False, blank=False, default="Your email address")

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='penpal')


    def __str__(self):
        return f'{self.name}'
