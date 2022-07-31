from pf_app.models.producto import Producto
from rest_framework import serializers
from pf_app.models.carrito import Carrito
from pf_app.models.user import User

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
        carrito = Carrito.objects.all
        usuario = User()
        producto = Producto()
        
        imprimir = [carrito.productos,carrito.cantidad, producto.objects.get(id_producto = carrito.productos)]
        print('ACÁ EMPIEZA LA IMPRESIÓN')
        print(imprimir)
        return {
            'id_usuario': usuario.id_usuario,
                'productos': carrito.productos,
                'cantidad': carrito.cantidad,
                'costo': producto.objects.get(id_producto = carrito.productos)
                }
            ##    'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno
            