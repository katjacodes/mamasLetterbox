from django.contrib import admin
from subscriptions.models import StripeCustomer, Subscription

# Register your models here.
admin.site.register(StripeCustomer)
admin.site.register(Subscription)

