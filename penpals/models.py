from django.db import models

from django_countries.fields import CountryField

# Create your models here.

"""
A penpal profile model for maintainining
searchable information to match penpals
"""

class PenpalProfile(models.Model):
    ENGLISH = 'ENG'
    SPANISH = 'SPA'
    FRENCH = 'FRA'
    GERMAN = 'DEU'
    PORTUGUESE = 'POR'
    LANGUAGE_CHOICES = [
        (ENGLISH, 'English'),
        (SPANISH, 'Spanish'),
        (FRENCH, 'French'),
        (GERMAN, 'German'),
        (PORTUGUESE, 'Portuguese'),
    ]
    language1 = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        null=False,
        blank=False,
    )
    language2 = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        blank=True,
        null=True,
    )
    language3 = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        blank=True,
        null=True,
    )

    name = models.CharField(max_length=50, null=False, blank=False, default="Your name")
    pronoun = models.CharField(max_length=50, null=False, blank=False, default="Your preferred pronoun/s)")
    age = models.IntegerField(null=False, blank=False, default="Your age")
    country = CountryField(null=False, blank=False)
    hobby1 = models.CharField(max_length=50, null=False, blank=False, default="A hobby")
    hobby2 = models.CharField(max_length=50, blank=True, null=True, default="Second hobby (optional)")
    hobby3 = models.CharField(max_length=50, blank=True, null=True, default="Third hobby (optional)")
    childAge1 = models.IntegerField(null=False, blank=False, default="Your child's age")
    childAge2 = models.IntegerField(blank=True, null=True, default="Second child's age (optional)")
    childAge3 = models.IntegerField(blank=True, null=True, default="Third child's age (optional)")
    childAge4 = models.IntegerField(blank=True, null=True, default="Fourth child's age (optional)")
    childAge5 = models.IntegerField(blank=True, null=True, default="Fifth child's age (optional)")
    email = models.EmailField(max_length=50, null=False, blank=False,  default="Your email address")

    def __str__(self):
        return f'{self.name}'
