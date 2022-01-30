from django.utils import timezone
from .models import Subscription


def get_active_subscription(user):
    """
    Function to determine duration of a user's subscription.
    Thank you to Benoit Blanchon for his help with these
    functions.
    """

    return Subscription.objects.filter(user=user, validUntil__gte=timezone.now()).order_by(('id')).first()


def is_user_subscribed(user):
    """
    Function to determine whether a user has an active subscription.
    """

    return Subscription.objects.filter(user=user, validUntil__gte=timezone.now()).exists()
