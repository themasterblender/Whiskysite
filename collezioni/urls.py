# urls.py per l'app 'collezioni'

from django.urls import path
from . import views

app_name = 'collezioni'
urlpatterns = [
    path('', views.collections_list, name='collections_list'),
    path('<int:id_collezione>/', views.collection_detail, name='collection_detail'),
    path('bottle/<int:id_bottle>/', views.bottle_detail, name='bottle_detail'),
]

