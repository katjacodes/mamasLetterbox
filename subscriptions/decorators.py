from functools import wraps
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import StripeCustomer

def is_user_subscribed(user):
    return StripeCustomer.objects.filter(user=user, validUntil__lte=timezone.now()).exists()


def subscription_required(func):
    @login_required
    @wraps(func)
    def inner(request, *args, **kwargs):        
        if is_user_subscribed(request.user):
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('subscriptions-home'))
    return inner