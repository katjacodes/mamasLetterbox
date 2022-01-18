from django.shortcuts import render
from .models import PenpalProfile


# Create your views here.


def penpal(request):
    penpals = 'penpals/penpal.html'
    context = {}

    return render(request, 'penpals/penpal.html', context)
