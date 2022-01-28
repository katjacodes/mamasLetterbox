from django.utils import timezone
from .models import Subscription

def get_active_subscription(user):
    return Subscription.objects.filter(user=user, validUntil__gte=timezone.now()).order_by(('id')).first()

def is_user_subscribed(user):
    return Subscription.objects.filter(user=user, validUntil__gte=timezone.now()).exists()
