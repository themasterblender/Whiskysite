from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse
from .forms import SignupForm

def index(request):
    # return HttpResponse("Welcome to Whiskysite!!! This is just a test page, not a real website")
    return render(request, 'index.html', {})


# 16/06/2018 Nuova funzione per la creazione di un utente con conferma della email inserita
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Whiskysite account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# 16/06/2018 Vecchia funzione per la creazione di un utente senza conferma della email inserita
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

# 16/06/2018 Questa funzione viene attivata dal click del nuovo utente sul link inviato via email
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return HttpResponseRedirect(reverse('user_created'))
    else:
        return HttpResponse('Activation link is invalid!')

    
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

