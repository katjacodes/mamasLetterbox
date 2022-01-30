from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='subscriptions-home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success, name='subscriptions-success'),
    path('cancel/', views.cancel, name='subscriptions-cancel'),
    path('webhook/', views.stripe_webhook),
]
