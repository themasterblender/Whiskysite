from django.shortcuts import render, get_object_or_404
from .models import Collezione, Bottle

def collections_list(request):
    collections = Collezione.objects.all()
    return render(request, 'collezioni/collections_list.html', {'collections': collections})

def collection_detail(request, id_collezione):
    coll = get_object_or_404(Collezione, id=id_collezione)
    bottles = Bottle.objects.filter(collezione_id=id_collezione)
    return render(request, 'collezioni/collection_detail.html', {'bottles': bottles, 'coll': coll})

def bottle_detail(request, id_bottle):
    bottle = get_object_or_404(Bottle, id=id_bottle)
    return render(request,'collezioni/bottle_detail.html', {'bottle': bottle})

