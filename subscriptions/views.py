import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_safe, require_POST
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from subscriptions.models import StripeCustomer

# Create your views here.


@login_required
def home(request):
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        return render(request, 'home.html', {
            'subscription': subscription,
            'product': product,
        })

    except StripeCustomer.DoesNotExist:
        print('Nah, that didn\'t work')
        return render(request, 'subscriptions/home.html')


@require_safe
def stripe_config(request):
    stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_config, safe=False)


@login_required
@require_safe
def create_checkout_session(request):
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
    return render(request, 'subscriptions/success.html')


@login_required
def cancel(request):
    return render(request, 'subscriptions/cancel.html')


@csrf_exempt
@require_POST
def stripe_webhook(request):
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
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
            validUntil=timezone.now() + timedelta(days=30)
        )
        print(user.username + ' just subscribed.')

    return JsonResponse({'status': 'success'})



def customer_portal(request):
    # Authenticate your user.
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.billing_portal.Session.create(
        customer='{{CUSTOMER_ID}}',
        return_url=request.build_absolute_uri(''),
    )
    return redirect(session.url)
