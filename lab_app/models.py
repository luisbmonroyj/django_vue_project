from django.db import models
# Create your models here.

class Producto(models.Model):
    id_producto = models.BigAutoField('id_producto', primary_key= True)
    nombre_producto = models.CharField('nombre_producto', max_length=50, unique=True, default=None)
    presentacion = models.CharField('presentacion', max_length=500, unique=False, default=None)
    precio = models.FloatField('precio', default= 0.0)

    #def __str__(self):
    #   return self.nombre_producto

class Articulo(models.Model):
    id_articulo = models.BigAutoField('id_producto', primary_key= True)
    cantidad = models.IntegerField('cantidad',default=0)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE,unique=True)
    p = Producto.objects.get(pk=id_producto.value_to_string)
    costo = p.precio * cantidad
    

    #def __str__(self):
    #    return {'id_producto':self.id_producto,'cantidad':self.cantidad}

