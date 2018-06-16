"""whiskysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home Page'),
    path('collezioni/', include('collezioni.urls')),
    path('signup/', views.signup, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('accounts/', include('django.contrib.auth.urls')),
    # 16/06/2018 path('register/', views.register, name='register_new_user'),
    path('register/', views.signup, name='register_new_user'),
    path('user_created/', views.user_created, name='user_created'),
    path('gallery/landscapes/', views.landscapes_gallery, name='landscapes_gallery'),
    path('gallery/villages/', views.villages_gallery, name='villages_gallery'),
    path('gallery/castles/', views.castles_gallery, name='castles_gallery'),
    path('gallery/distilleries/', views.distilleries_gallery, name='distilleries_gallery'),
]
