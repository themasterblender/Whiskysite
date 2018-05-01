# urls.py per l'app 'collezioni'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='collezioni'),
]
