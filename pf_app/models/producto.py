from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class Producto(models.Model):
    id_producto = models.BigAutoField('id_producto', primary_key= True)
    nombre_producto = models.CharField('nombre_producto', max_length=50, unique=True, default=None)
    presentacion = models.CharField('presentacion', max_length=500, unique=False, default=None)
    precio = models.FloatField('precio', default= 0.0)
    
    #username = models.CharField('usuario',max_length=30, unique=True ,default='loser')