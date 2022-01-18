from django.shortcuts import render
from .models import Stationery

# Create your views here.

def all_stationery(request):
    """ A view to show all stationery items """

    stationery_items = Stationery.objects.all()

    context = {
        'stationery_items': stationery_items,
    }

    return render(request, 'stationery/all_stationery.html', context)
