### Ya es funcional

from django.db import models

class Status(models.Model):
    #models.Model means that Status is a Model
    id_status = models.BigAutoField('id_status', primary_key= True)
    descripcion = models.CharField('descripcion', max_length=50, unique=True)
    
    def __str__(self):
        return self.descripcion

    #esta tabla tiene los 6 estados posibles de una orden(pedido)
    #pagado,preparado,congelado,empacado,enviado,recibido
    # I WOULD LIKE TO KNOW HOW TO FILL THE TABLE WITH THIS VALUES FROM WITHIN

#SCRIPT para crear los estados de pedido
#estadosList = ['pagado','preparado','congelado','empacado','enviado','recibido']
#for i in estadosList:
    #estado = Status(descripcion=i)
    #estado.save()

