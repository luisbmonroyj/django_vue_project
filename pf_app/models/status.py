from django.db import models

class Status(models.Model):
    id_status = models.BigAutoField('id_status', primary_key= True)
    descripcion = models.CharField('descripcion', max_length=50, unique=True)
    
    #esta tabla tiene los 6 estados posibles de una orden(pedido)
    #pagado,preparado,congelado,empacado,enviado,recibido
    