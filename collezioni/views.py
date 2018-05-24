from django.shortcuts import render, get_object_or_404
from .models import Collezione, Bottle, Category
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import CreateCollectionForm, CreateBottleForm
from datetime import datetime
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def collections_list(request):
    collections = Collezione.objects.all()
    return render(request, 'collezioni/collections_list.html', {'collections': collections})

@login_required
def collection_detail(request, id_collezione):
    coll = get_object_or_404(Collezione, id=id_collezione)
    bottles = Bottle.objects.filter(collezione_id=id_collezione)
    return render(request, 'collezioni/collection_detail.html', {'bottles': bottles, 'coll': coll})

@login_required
def bottle_detail(request, id_bottle):
    bottle = get_object_or_404(Bottle, id=id_bottle)
    return render(request,'collezioni/bottle_detail.html', {'bottle': bottle})

@login_required
def bottle_list(request):
    bottles = Bottle.objects.all()
    return render(request, 'collezioni/bottle_list.html', {'bottles': bottles})

@login_required
def collection_create(request):
    """
    View function for creating a new collection owned by the current user
    """
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = CreateCollectionForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            coll = Collezione()
            coll.title = form.cleaned_data['title']
            coll.text = form.cleaned_data['text']
            coll.owner = request.user
            coll.published_date = datetime.now()            
            coll.save()
            bott = Bottle()
            bott.collezione = Collezione.objects.get(id=coll.id)
            bott.whisky_type = form.cleaned_data['whisky_type']
            bott.name = form.cleaned_data['name']
            bott.distillery = form.cleaned_data['distillery']
            bott.bottler = form.cleaned_data['bottler']
            bott.age = form.cleaned_data['age']
            bott.year_bottled = form.cleaned_data['year_bottled']
            bott.purchased_date = form.cleaned_data['purchased_date']
            bott.purchased_place = form.cleaned_data['purchased_place']
            bott.price = form.cleaned_data['price']
            bott.bottle_code = form.cleaned_data['bottle_code']
            bott.created_date = datetime.now()
            bott.published_date = datetime.now()
            bott.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('collezioni:bottle_create', args=(coll.id,'collectionsaved')))
    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateCollectionForm()
    return render(request, 'collezioni/collection_create.html', {'form': form})

@login_required
def bottle_create(request, id_coll, previousaction):
    coll = get_object_or_404(Collezione, pk=id_coll)
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = CreateBottleForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            bott = Bottle()
            bott.collezione = coll
            bott.whisky_type = form.cleaned_data['whisky_type']
            bott.name = form.cleaned_data['name']
            bott.distillery = form.cleaned_data['distillery']
            bott.bottler = form.cleaned_data['bottler']
            bott.age = form.cleaned_data['age']
            bott.year_bottled = form.cleaned_data['year_bottled']
            bott.purchased_date = form.cleaned_data['purchased_date']
            bott.purchased_place = form.cleaned_data['purchased_place']
            bott.price = form.cleaned_data['price']
            bott.bottle_code = form.cleaned_data['bottle_code']
            bott.created_date = datetime.now()
            bott.published_date = datetime.now()
            bott.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('collezioni:bottle_create', args=(id_coll,'bottlesaved')))
    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateBottleForm()
    return render(request, 'collezioni/bottle_create.html', {'form': form, 'coll': coll, 'previousaction': previousaction})
    
class CollezioneUpdate(LoginRequiredMixin, UpdateView):
    model = Collezione
    fields = ['title','text']
    success_url = reverse_lazy('collezioni:collections_list')

class CollezioneDelete(LoginRequiredMixin, DeleteView):
    model = Collezione
    success_url = reverse_lazy('collezioni:collections_list')

