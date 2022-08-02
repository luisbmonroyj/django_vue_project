from django.db import models
from pf_app.models import User
from pf_app.models import Status

class Pedido(models.Model):
    id_pedido = models.BigAutoField('id_pedido', primary_key= True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField('total',default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    
    