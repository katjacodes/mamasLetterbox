from django.db import models

from django.contrib.auth.models import User
from django_countries.fields import CountryField

from home.models import Item


# Create your models here.
class WriterProfile(models.Model):
    """
    A writer profile model for maintainining
    searchable information to match penpals
    """
    writer = models.OneToOneField(Item, User, on_delete=models.CASCADE)

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

    default_username = models.CharField(max_length=50, null=False, blank=False)
    default_first_name = models.CharField(max_length=50, null=False, blank=False)
    default_last_name = models.CharField(max_length=50, null=False, blank=False)
    default_pronoun = models.CharField(max_length=50, null=False, blank=False)
    default_age = models.IntegerField(null=False, blank=False)
    default_country = CountryField(null=False, blank=False)
    hobby1 = models.CharField(max_length=50, null=False, blank=False, default="First Hobby")
    hobby2 = models.CharField(max_length=50, blank=True, null=True, default="Second Hobby")
    hobby3 = models.CharField(max_length=50, blank=True, null=True, default="Third Hobby")
    childAge1 = models.IntegerField(null=False, blank=False, default=0)
    childAge2 = models.IntegerField(blank=True, null=True, default=0)
    childAge3 = models.IntegerField(blank=True, null=True, default=0)
    childAge4 = models.IntegerField(blank=True, null=True, default=0)
    childAge5 = models.IntegerField(blank=True, null=True, default=0)
    default_email = models.EmailField(max_length=50, null=False, blank=False, default="myemail@email.com")

    def __str__(self):
        return f'{self.default_first_name}'
