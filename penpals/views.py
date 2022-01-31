"""
Code taken from Code Institute's Hello Django module
and edited to fit project needs.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from subscriptions.decorators import subscription_required

from .models import PenpalProfile
from .forms import PenpalForm


@login_required
def basicdetails(request):
    """
    Basic profile details, visible
    to registered users without
    a subscription
    """

    penpals = PenpalProfile.objects.all()
    context = {'penpals': penpals}
    return render(request, 'penpals/basic_details.html', context)


@subscription_required
def penpal_list(request):
    """
    List of registered penpals with
    option to see additional details,
    accessible only to registered
    users with a subscription.
    """

    penpals = PenpalProfile.objects.all()
    context = {'penpals': penpals}
    return render(request, 'penpals/penpal_list.html', context)


@login_required
def my_penpal_profile(request):
    """ Registered user's own penpal profile """

    if hasattr(request.user, 'penpal'):
        context = {'penpal': request.user.penpal}
        return render(request, 'penpals/my_details.html', context)
    else:
        return redirect(reverse('penpal_create'))


@login_required
def my_penpal_profile_edit(request):
    """ Profile editing page """

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

    penpal = get_object_or_404(Penpal, id=penpal_id)
    context = {'penpal': penpal}
    return render(request, 'penpals/penpal_detail.html', context)


@login_required
def penpal_create(request):
    """
    Penapal profile creation functionality
    for registered users
    """

    if request.method == 'POST':
        form = PenpalForm(request.POST)
        if form.is_valid():
            new_profile = PenpalProfile.objects.create(
                user=User.objects.get(pk=request.user.id),
            )
            new_profile.save()
            return redirect('penpal_list')
    else:
        form = PenpalForm()
    context = {
        'form': form,
    }
    return render(request, 'penpals/penpal_create.html', {'form': form})


@login_required
def penpal_delete(request):
    """
    Penapal profile deletion functionality
    for registered users
    """

    if hasattr(request.user, 'penpal'):
        penpal = request.user.penpal
        penpal.delete()
        messages.success(request, f'Penpal profile successfully deleted!')

    else:
        return redirect(reverse('penpal_create'))
