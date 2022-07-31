from django.db import models
from pf_app.models import producto
from pf_app.models import user

class Carrito(models.Model):
    #producto = producto.Producto()
    #id_carrito = models.BigAutoField('id_carrito', primary_key= True)
    id_usuario = models.ForeignKey(user.User, on_delete=models.CASCADE)
    productos = models.ForeignKey(producto.Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad', default= 1)
    #costo = producto.precio
    #valor = costo * cantidad
    """
    def __str__(self):
        diccionario = {
            'producto': self.producto,
            'id_carrito': self.id_carrito,
            'cantidad': self.cantidad,
            'productos':self.productos
        }
        return diccionario
    """    
    
    #username = models.CharField('usuario',max_length=30, unique=True ,default='loser')