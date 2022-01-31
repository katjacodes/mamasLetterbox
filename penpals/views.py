"""
Code taken from Code Institute's Hello Django module
and edited to fit project needs.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from subscriptions.helpers import is_user_subscribed
from .models import PenpalProfile
from .forms import PenpalForm


@login_required
def penpal_list(request):
    """
    List of registered penpals with
    option to see additional details,
    for registered users with a subscription
    and a button to the subscription page
    for registered users without a subscription.
    """

    penpals = PenpalProfile.objects.exclude(user__is_active=False)
    context = {'penpals': penpals}
    if is_user_subscribed(request.user):
        return render(request, 'penpals/penpal_list.html', context)
    else:
        return render(request, 'penpals/basic_details.html', context)


@login_required
def my_penpal_profile(request):
    """ Registered user's own penpal profile """

    if hasattr(request.user, 'penpal'):
        context = {'penpal': request.user.penpal}
        return render(request, 'penpals/my_details.html', context)
    else:
        return redirect('penpal_me_edit')


@login_required
def my_penpal_profile_edit(request):
    """ 
    Profile creation and editing page.
    Thank you to Benoit Blanchon for
    suggesting to combine these tow
    functionalities.
    """

    if hasattr(request.user, 'penpal'):
        penpal = request.user.penpal
    else:
        penpal = PenpalProfile(user=request.user)
    if request.method == 'POST':
        form = PenpalForm(request.POST, instance=penpal)
        if form.is_valid():
            form.save()
            return redirect('penpal_me')
    else:
        form = PenpalForm(instance=penpal)
    context = {'form': form}
    return render(request, 'penpals/penpal_edit.html', context)


@login_required
def penpal_detail(request, penpal_id):
    """ A registered user's own penpal profile """

    penpal = get_object_or_404(PenpalProfile,
                               id=penpal_id, user__is_active=True)
    context = {'penpal': penpal}
    return render(request, 'penpals/penpal_detail.html', context)


@login_required
def penpal_delete(request):
    """
    Penapal profile deletion functionality
    for registered users. Thank you to Benoit Blanchon for
    teaching me about the user.is_active fied and the
    advantages of deactivating a user profile vs.
    deleting it.
    """

    request.user.is_active = False
    request.user.save()
    messages.success(request, 'Penpal profile successfully deleted!')
    return redirect('home')
