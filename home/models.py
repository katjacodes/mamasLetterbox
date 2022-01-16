from django.db import models

from django_countries.fields import CountryField


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    pronoun = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    country = CountryField(null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
