from functools import wraps
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Subscription
from  .helpers import is_user_subscribed


def subscription_required(func):
    @login_required
    @wraps(func)
    def inner(request, *args, **kwargs):        
        if is_user_subscribed(request.user):
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('subscriptions-home'))
    return inner