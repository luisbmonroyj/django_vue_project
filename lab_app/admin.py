from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Producto)
admin.site.register(Articulo)