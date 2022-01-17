from django.shortcuts import render, redirect
from .models import WriterProfile
from .forms import WriterProfileForm

# Create your views here.


def writer(request):
    writers = WriterProfile.objects.all().filter(username="streberkatze")
    context = {
        'writers': writers
    }

    return render(request, 'writers/writer.html', context)


def add_writer(request):
    profiles = WriterProfile.objects.all().filter(name="streberkatze")
    context = {
        'writers': writers
    }

    if request.method == 'POST':
        info = ItemForm(request.POST)
        if info.is_valid():
            info.save()
            return redirect('writers/writer.html', context)
            
    else:
        info = ItemForm()
        
    return render(request, 'writers/add_writer.html', {'form':info})


def edit_writer(request):
    return render(request, 'home/edit_writer.html')
