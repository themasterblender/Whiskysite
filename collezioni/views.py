from django.shortcuts import render
from .models import Collezione, Bottle

def index(request):
    colls = Collezione.objects.all()
    return render(request, 'collezioni/collezioni.html', {'colls': colls})

def collezione_detail(request, id_collezione):
    bottles = Bottle.objects.filter(collezione_id=id_collezione)
    collezione = Collezione.objects.get(id=id_collezione)
    return render(request, 'collezioni/collezione_detail.html', {'bottles': bottles, 'collezione': collezione})

def bottle_detail(request, id_bottle):
    b = Bottle.objects.get(id=id_bottle)
    return render(request,'collezioni/bottle_detail.html', {'bottle': b})

