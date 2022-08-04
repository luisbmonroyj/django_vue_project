from django.db import models
from pf_app.models import Producto
from pf_app.models import User
from pf_app.models import pedido 
 
class Carrito(models.Model):
    id_carrito = models.BigAutoField('id', primary_key= True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    ## Diccionario
    cantidad = models.IntegerField('cantidad', default= 1)
    costo = models.FloatField('costo',default=0)
    id_pedido = models.ForeignKey(pedido.Pedido, default= None, on_delete=models.CASCADE)
    
    
    #def save(self, **kwar):

    #    print(carritoData)
                
    #    return Response(carritoData, status = status.HTTP_201_CREATED)
    
    
    
    #la mejor idea hasta el momento es llenar costo con 0 y luego editar el campo
    #con la operacion cantidad * Producto.precio
    #valor = models.FloatField(costo*cantidad ,default=0)
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