from pf_app.models.carrito import Carrito
from pf_app.models.producto import Producto
from rest_framework import serializers


class CarritoSerializer(serializers.ModelSerializer):
        #userData = UserData()
    class Meta:
        model = Carrito
        fields = '__all__'
        #['id_usuario','password','apellido','nombre','telefono','direccion','estado']

    def create(self,validated_data):
        carritoInstance = Carrito.objects.create(**validated_data)
        return carritoInstance
    
    def to_representation(self, object):
        producto = Carrito.objects.get(id_producto=object.id_producto)
        return {'id_producto': producto.id_producto,
                'nombre_producto': producto.nombre_producto,
                'presentacion': producto.presentacion,
                'precio': producto.precio,
                }
            #    'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno

            
    