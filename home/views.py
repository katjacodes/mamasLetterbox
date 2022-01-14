from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def penpals(request):
    profiles = Item.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'home/penpals.html', context)


def profile(request):
    profiles = Item.objects.all().filter(name="Katja")
    context = {
        'profiles': profiles
    }

    return render(request, 'home/profile.html', context)


def add_profile(request):
    profiles = Item.objects.all().filter(name="Katja")
    context = {
        'profiles': profiles
    }

    if request.method == 'POST':
        info = ItemForm(request.POST)
        if info.is_valid():
            info.save()
            return redirect('home/home.html', context)
            
    else:
        info = ItemForm()
        
    return render(request, 'home/add_profile.html', {'form':info})


def edit_profile(request):
    return render(request, 'home/edit_profile.html')
