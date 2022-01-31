""" Custom-created decorators """

from functools import wraps
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .helpers import is_user_subscribed


def subscription_required(func):
    """
    A decorator to check if a user is subscribed and redirect
    unsubscribed users to the subscription page.
    Thank you to Benoit Blanchon for his help with this
    approach.
    """

    @login_required
    @wraps(func)
    def inner(request, *args, **kwargs):
        if is_user_subscribed(request.user):
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('subcribe'))
    return inner
