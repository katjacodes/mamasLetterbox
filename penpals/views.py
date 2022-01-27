from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import PenpalProfile
from .forms import PenpalForm


# CRUD Functionality: Create Read Update Delete
# Create
# Read: List view, Detail view
# Update:
# Delete


@login_required
def penpal_list(request):
    penpals = PenpalProfile.objects.all()
    context = {'penpals': penpals}
    return render(request, 'penpals/penpal_list.html', context)


@login_required
def my_penpal_profile(request):
    if hasattr(request.user, 'penpal'):
        context = {'penpal': request.user.penpal}
        return render(request, 'penpals/penpal_detail.html', context)
    else:
        return redirect(reverse('penpal_me_edit'))


@login_required
def my_penpal_profile_edit(request):
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
    penpals = get_object_or_404(Penpal, id=penpal_id)
    context = {'penpal': penpal}
    return render(request, 'penpals/penpal_detail.html', context)


@login_required
def penpal_create(request):
    if request.method == 'POST':
        form = PenpalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penpal_list')
    else:
        form = PenpalForm()
    context = {
        'form': form,
    }
    return render(request, 'penpals/penpal_create.html', {'form': form})
