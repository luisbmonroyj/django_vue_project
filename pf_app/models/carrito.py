"""
from django.db import models
from models import producto

class Carrito(models.Model):
    pedido = models.ForeignKey('id_pedido')
    producto = producto.Producto()
    id_carrito = models.BigAutoField('id_carrito', primary_key= True)
    cantidad = models.IntegerField('cantidad', default= 0)
    productos = models.ForeignKey(producto, on_delete=models.CASCADE)
    #costo = producto.precio
    #valor = costo * cantidad
    
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