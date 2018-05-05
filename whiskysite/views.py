from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Whiskysite!!! This is just a test page, not a real website")
