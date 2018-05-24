from django.contrib import admin

from .models import Collezione
from .models import Bottle
from .models import Category

admin.site.register(Collezione)
admin.site.register(Bottle)
admin.site.register(Category)
