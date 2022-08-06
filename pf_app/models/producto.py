### Ya es funcional

from django.db import models

class Producto(models.Model):
    id_producto = models.BigAutoField('id_producto', primary_key= True)
    nombre_producto = models.CharField('nombre_producto', max_length=50, unique=True, default=None)
    presentacion = models.CharField('presentacion', max_length=500, unique=False, default=None)
    precio = models.FloatField('precio', default= 0.0)
