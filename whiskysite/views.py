from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse

def index(request):
    # return HttpResponse("Welcome to Whiskysite!!! This is just a test page, not a real website")
    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('user_created'))
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
    
def user_created(request):
    return render(request, 'user_created.html', {})
    
def landscapes_gallery(request):
    return render(request, 'landscapes_gallery.html', {})
    
def villages_gallery(request):
    return render(request, 'villages_gallery.html', {})
    
def castles_gallery(request):
    return render(request, 'castles_gallery.html', {})

def distilleries_gallery(request):
    return render(request, 'distilleries_gallery.html', {})

