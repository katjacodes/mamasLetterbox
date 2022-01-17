from django.db import models

from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class WriterProfile(models.Model):
    """
    A writer profile model for maintainining
    searchable information to match penpals
    """

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
    )
    language3 = models.CharField(
        max_length=3,
        choices=LANGUAGE_CHOICES,
        default=ENGLISH,
        blank=True,
    )

    default_username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="default_username")
    default_first_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="default_first_name")
    default_last_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="default_last_name")
    pronoun = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    country = CountryField(null=False, blank=False)
    hobby1 = models.CharField(max_length=50, null=False, blank=False, default="First Hobby")
    hobby2 = models.CharField(max_length=50, blank=True, default="Second Hobby")
    hobby3 = models.CharField(max_length=50, blank=True, default="Third Hobby")
    childAge1 = models.IntegerField(null=False, blank=False, default=0)
    childAge2 = models.IntegerField(blank=True, default=0)
    childAge3 = models.IntegerField(blank=True, default=0)
    childAge4 = models.IntegerField(blank=True, default=0)
    childAge5 = models.IntegerField(blank=True, default=0)
    default_email = models.OneToOneField(User, on_delete=models.CASCADE, related_name="default_email")

    def __str__(self):
        return f'{self.default_username}'
