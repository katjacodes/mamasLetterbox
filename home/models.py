from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Item(models.Model):
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
        blank=False
    )
    language2 = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        blank=True
    )
    language3 = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        blank=True
    )

    name = models.CharField(max_length=50, null=False, blank=False)
    pronoun = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    country = CountryField(null=False, blank=False)
    hobby1 = models.CharField(max_length=50, null=False, blank=False)
    hobby2 = models.CharField(max_length=50, blank=True)
    hobby3 = models.CharField(max_length=50, blank=True)
    childAge1 = models.IntegerField(null=False, blank=False)
    childAge2 = models.IntegerField(blank=True)
    childAge3 = models.IntegerField(blank=True)
    childAge4 = models.IntegerField(blank=True)
    childAge5 = models.IntegerField(blank=True)
    email = models.EmailField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
