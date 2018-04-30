from django.contrib import admin

from .models import Collezione
from .models import Bottle

admin.site.register(Collezione)
admin.site.register(Bottle)
