from pf_app.models.producto import Producto
from rest_framework import serializers
from pf_app.models.carrito import Carrito
#from pf_app.models.user import User

class CarritoSerializer(serializers.ModelSerializer):
    #userData = UserData()
    class Meta:
        model = Carrito
        fields = '__all__'
        #['id_carrito','id_usuario','productos','cantidad','costo','id_pedido']

    def create(self,validated_data):
        carritoInstance = Carrito.objects.create(**validated_data)
        return carritoInstance
    
    def to_representation(self, object):
        #carrito = Carrito.objects.all()
        #usuario = User()
        #Producto.objects.get(id_producto=1).carrito_se.all()
        #Producto.objects.all().filter(carrito__id_usuario=1)
        #carrito.objects.create(id_usuario=1,cantidad=5)
        #productos=Producto.objects.get(id_producto=1))
        carrito = Carrito()
        Carrito.objects.filter(producto__id_producto=1)
        productos_json = carrito.
        return {
            'id_usuario': carrito.id_usuario,
            'productos_usuario': carrito.productos,
            'cantidad': carrito.cantidad,
            }
                #podriamos usar Carrito.id_usuario? Porque ese dato esta guardado en el META de carrito
                #podriamos usar el diccionario que estamos usando en Pedido? el que relaciona id_producto:cantidad?
                #'costo': producto.objects.get(id_producto = carrito.productos)
            ##   'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno
            