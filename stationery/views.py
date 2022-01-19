from django.shortcuts import render, get_object_or_404
from .models import Stationery

# Create your views here.

def all_stationery(request):
    """ A view to show all stationery items """

    stationery_items = Stationery.objects.all()

    context = {
        'stationery_items': stationery_items,
    }

    return render(request, 'stationery/all_stationery.html', context)


def stationery_detail(request, stationery_item_id):
    """ A view to show individual stationery item details """

    stationery_item = get_object_or_404(Stationery, pk=stationery_item_id)

    context = {
        'stationery_item': stationery_item,
    }

    return render(request, 'stationery/stationery_detail.html', context)
