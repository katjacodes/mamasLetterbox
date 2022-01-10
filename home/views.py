from django.shortcuts import render
from .models import Item

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
