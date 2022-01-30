from django.contrib.auth.models import User
from django.db import models


class StripeCustomer(models.Model):
    """
    Model to create a Stripe customer.
    """

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.user}'


class Subscription(models.Model):
    """
    Model to save subscription data. Thank you to Benoit Blanchon
    for his help with this model.
    """

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    stripeSubscriptionId = models.CharField(max_length=255)
    validUntil = models.DateTimeField()

    def __str__(self):
        return f'{self.user}'
