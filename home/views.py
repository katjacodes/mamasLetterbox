from django.shortcuts import render
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
    info = ItemForm()
    return render(request,"home/add_profile.html",{'form':info})
