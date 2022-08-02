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
        #carrito = Carrito.objects.all()
        carrito = Carrito()
        print('IMPRESIÓN DE CARRITO')
        print(carrito)
        usuario = User()
        print('IMPRESIÓN DE USUARIO')
        print(usuario)
        producto = Producto()
        print('IMPRESIÓN DE PRODUCTO')
        print(producto)
        prodID = carrito.objects.get(id_usuario=1).productos.id_producto
        print('IMPRESIÓN DEL idPRODUCTO del carrito')
        print(prodID)  
        queryset = carrito.objects.filter(productos=1)
        Producto.objects.get(id_producto=1).carrito_se.all()
        #si en la llave foranea se usa related_name= 'carritos'
        #Se puede usar
        # Producto.objects.get(id_producto=1).carritos.all()
        Producto.objects.all().filter(carrito__id_usuario=1)
        #esta instruccion sirve para crear un dato 
        carrito.objects.create(id_usuario=1,cantidad=5,
            productos=Producto.objects.get(id_producto=1))
        Carrito.objects.filter(producto__id_producto=1)
        #probar con dos argumentos para filtrar los productos de un usuario



        # imprimir = [carrito.productos,carrito.cantidad, producto.objects.get(id_producto = carrito.productos)]
        # print('ACÁ EMPIEZA LA IMPRESIÓN')
        # print(imprimir)
        return {
            'id_usuario': usuario.id_usuario,
                'productos': carrito.productos,
                'cantidad': carrito.cantidad,
                #'costo': producto.objects.get(id_producto = carrito.productos)
                }
            ##    'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno
            