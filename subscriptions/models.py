from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.user.username
    

class Subscription(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    stripeSubscriptionId = models.CharField(max_length=255)
    validUntil = models.DateTimeField()

    def __str__(self):
        return self.user.username