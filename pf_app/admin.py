from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.producto import Producto
from .models.status import Status
from .models.pedido import Pedido
from .models.carrito import Carrito

admin.site.register(User)
admin.site.register(Producto)
admin.site.register(Status)
admin.site.register(Pedido)
admin.site.register(Carrito)


#admin.site.register(Account)