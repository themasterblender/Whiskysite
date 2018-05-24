# urls.py per l'app 'collezioni'

from django.urls import path
from . import views

app_name = 'collezioni'
urlpatterns = [
    path('', views.collections_list, name='collections_list'),
    path('<int:id_collezione>/', views.collection_detail, name='collection_detail'),
    path('bottle/<int:id_bottle>/', views.bottle_detail, name='bottle_detail'),
    path('bottle_list/', views.bottle_list, name='bottle_list'),
    path('coll/create/', views.collection_create, name='collection_create'),
    path('bottle/create/<int:id_coll>/<str:previousaction>', views.bottle_create, name='bottle_create'),
    path('coll/<int:pk>/update/', views.CollezioneUpdate.as_view(), name='collection_update'),
    path('coll/<int:pk>/delete/', views.CollezioneDelete.as_view(), name='collection_delete'),
]

