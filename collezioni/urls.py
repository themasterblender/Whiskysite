# urls.py per l'app 'collezioni'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='collezioni'),
    path('<int:id_collezione>/', views.collezione_detail, name='Collection detail'),
    path('bottle/<int:id_bottle>/', views.bottle_detail, name='Bottle detail'),
]
