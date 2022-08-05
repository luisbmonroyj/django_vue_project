from pf_app.models.producto import Producto
from rest_framework import serializers
from pf_app.models.carrito import Carrito

class CarritoSerializer(serializers.ModelSerializer):
    #userData = UserData()
    class Meta:
        model = Carrito
        fields = '__all__'
        #['id_carrito','id_usuario','productos','cantidad','costo','id_pedido']

    def create(self,validated_data):
        carritoInstance = Carrito.objects.create(**validated_data)
        return carritoInstance
    #Tiene que crearse primero un pedido y enviarle el id_pedido como argumento dentro de object
    def to_representation(self, object):
        cart = Carrito.object.get(id_usuario=object.id_usuario,id_pedido=object.id_pedido)
        return {
            'id_usuario': cart.id_usuario,
            'productos': cart.productos,
            'cantidad': cart.cantidad,
            }
                #podriamos usar Carrito.id_usuario? Porque ese dato esta guardado en el META de carrito
                #podriamos usar el diccionario que estamos usando en Pedido? el que relaciona id_producto:cantidad?
                #'costo': producto.objects.get(id_producto = carrito.productos)
            ##   'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno
            
        #productos_json = carrito
        
        #carrito = Carrito()
        #carrito = Carrito.objects.all()
        #usuario = User()
        #Carrito.objects.filter(producto__id_producto=1)
        