from django.db import models

from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class PenpalProfile(models.Model):
    """
    A penpal profile model for maintainining
    searchable information to match penpals
    """
    user = models.OneToOneField (User, on_delete=models.CASCADE)
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

    def __str__(self):
        return f'{self.user.username}'