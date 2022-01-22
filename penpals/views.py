from django.shortcuts import render, get_object_or_404

from .models import PenpalProfile
from .forms import PenpalForm


# Create your views here.
def searchpenpals(request):
    penpals = PenpalProfile.objects.all()
    context = {
        'penpals': penpals
    }
    return render(request, 'penpals/searchpenpals.html', context)


def penpal(request):
    penpals = PenpalProfile.objects.all().filter(name="Katja")
    context = {
        'penpals': penpals
    }

    return render(request, 'penpals/penpal.html', context)


def add_penpal(request):
    profiles = PenpalProfile.objects.all().filter(name="Katja")
    context = {
        'penpals': penpals
    }

    if request.method == 'POST':
        info = PenpalForm(request.POST)
        if info.is_valid():
            info.save()
            return redirect('penapals/penpal.html', context)
            
    else:
        info = ItemForm()
        
    return render(request, 'penpals/add_penpal.html', {'form':info})


def edit_penpal(request):
    return render(request, 'penpals/edit_penpal.html')
