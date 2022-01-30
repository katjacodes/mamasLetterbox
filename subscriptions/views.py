"""
Code taken from https://testdriven.io/blog/django-stripe-subscriptions/ and edited to fit project needs with the support of Benoit Blanchon.
"""

from datetime import datetime
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_safe, require_POST
from django.urls import reverse

from django.utils.timezone import utc

from subscriptions.models import StripeCustomer, Subscription
from .helpers import get_active_subscription


@login_required
def home(request):
    """
    A view to display the subscriptions page.
    """

    try:
        # Retrieve the subscription & product
        subscription = get_active_subscription(request.user)

        if subscription:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe_subscription = stripe.Subscription.retrieve(subscription.stripeSubscriptionId)
            product = stripe.Product.retrieve(stripe_subscription.plan.product)
        else:
            stripe_subscription = None
            product = None

        return render(request, 'subscriptions/home.html', {
            'subscription': stripe_subscription,
            'product': product,
        })

    except StripeCustomer.DoesNotExist:
        print('Nah, that didn\'t work')
        return render(request, 'subscriptions/home.html')


@require_safe
def stripe_config(request):
    """Stripe key"""

    stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_config, safe=False)


@login_required
@require_safe
def create_checkout_session(request):
    """
    A view to create a chckout session.
    """

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        client_reference_id=request.user.id,
        success_url=request.build_absolute_uri(reverse('subscriptions-success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('subscriptions-cancel')),
        payment_method_types=['card'],
        mode='subscription',
        line_items=[
            {
                'price': settings.STRIPE_PRICE_ID,
                'quantity': 1,
            }
        ]
    )

    # return JsonResponse({'sessionId': checkout_session['id']})
    return redirect(checkout_session.url)


@login_required
def success(request):
    """
    A view to display a success page upon successful checkout
    """

    return render(request, 'subscriptions/success.html')


@login_required
def cancel(request):
    """
    A view to display a cancel page upon a canceled checkout
    """

    return render(request, 'subscriptions/cancel.html')


@csrf_exempt
@require_POST
def stripe_webhook(request):
    """
    Stripe webhook
    """

    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    if not sig_header:
        return HttpResponseBadRequest("Signature missing")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponseBadRequest("Invalid payload")
    except stripe.error.SignatureVerificationError:
        return HttpResponseBadRequest("Invalid signature")

    # if event['type']  in ['checkout.session.completed', 'invoice.paid', 'invoice.payment_failed']:
    #    print("Event data", event)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        _, created = StripeCustomer.objects.update_or_create(
            user=user,
            defaults={
                'stripeCustomerId': stripe_customer_id,
            }
        )
        if created:
            print(user.username, 'associated with stripe id', stripe_customer_id)

    if event['type'] == 'invoice.paid':
        session = event['data']['object']

        # Fetch all the required data from session
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')
        subscription_end = session["lines"]["data"][0]['period']['end']

        stripe_customer = StripeCustomer.objects.filter(stripeCustomerId=stripe_customer_id).select_related('user').first()
        if not stripe_customer:
            return HttpResponseBadRequest("Unknown stripe customer id")
        user = stripe_customer.user

        # Get the user and create a new StripeCustomer
        Subscription.objects.create(
            user=user,
            stripeSubscriptionId=stripe_subscription_id,
            validUntil=datetime.fromtimestamp(subscription_end, tz=utc)
        )
        print(user.username + ' just subscribed.')

    return JsonResponse({'status': 'success'})
