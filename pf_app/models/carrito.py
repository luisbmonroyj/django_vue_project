from django.db import models
from pf_app.models import Producto
from pf_app.models import User

class Carrito(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad', default= 1)
    
    

    
    
    
    
    
    
    
    
    
    
    #id_carrito = models.BigAutoField('id_carrito', primary_key= True)
    
    #productos = models.ForeignKey(producto.Producto, on_delete=models.CASCADE)
    #costo = Producto.objects.all().annotate()
    #costo = models.FloatField(Producto.precio,default=8)
#    valor = costo.float
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