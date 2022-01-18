from django.shortcuts import render, get_object_or_404

from .models import PenpalProfile
from .forms import PenpalProfileForm


# Create your views here.

def penpal(request):
    """ Display the penpal's profile. """
    penpal = get_object_or_404(PenpalProfile, user=request.user)

    if request.method == 'POST':
        form = PenpalProfileForm(request.POST, instance=penpal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))

    template = 'penpals/penpal.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)