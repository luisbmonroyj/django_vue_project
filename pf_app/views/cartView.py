from posixpath import split
from tkinter import CENTER
from rest_framework import status,views
from rest_framework.response import Response
#from pf_app.models.carrito import Carrito
from pf_app.serializers.pedidoSerializer import PedidoSerializer
from pf_app.serializers.carritoSerializer import CarritoSerializer
from pf_app.models.producto import Producto
from pf_app.models.pedido import Pedido
from pf_app.models.carrito import Carrito


#from pf_app.serializers.productoSerializer import ProductoSerializer

class CarritoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        #serializer = CarritoSerializer(data = request.data) #llama al metodo create de carritoSerializer
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        
        #posiblemente no lo necesite
        userid = request.data['id_usuario']
        #lista debe tener las llaves y los valores del segundo elemento de del diccionario carritoData
        lista = request.data['productos']#segun el ejemplo, esta linea es
        #{'1': 4, '2': 8, '3': 12, '4': 16}
        total = 0
        costos = {}
        productosDB = Producto.objects.all()
        h = 0
        for i in lista:
            # i -> diccionario
            for z, l in i.items():
                costo = 0
                productoDB = productosDB.get(pk=int(z))
                costo = productoDB.precio * l
                costos[h] = costo
                h += 1
                total += costo   #### Acá se obtiene el total TOTAL
        usuario = request.data['id_usuario']
        pedidoCompleto = Pedido(usuario, total)
        pedidoCompleto.save()
        
        ##No tocar
        
        #serializer = CarritoSerializer(data = request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #lista_retorno = []
        for i in lista: 
            
            for z, l in i.items():
                productoDB = productosDB.get(pk=int(z))
                print('Printiando Z'.center(50, '*'))
                print(type(z))
                print('Printiando Z'.center(50, '*'))
                # carritoData = {
                #     'id_pedido':pedidoCompleto.id_pedido,
                #     'productos': z,
                #     'cantidad':l,
                #     'costo':productoDB.precio * l
                # }
                producto = Producto.objects.all().get(pk=int(z))
                carrito_entrega = Carrito(id_pedido = pedidoCompleto, productos = producto, cantidad = l, costo = productoDB.precio * l)
                carrito_entrega.save()
        return Response(status = status.HTTP_201_CREATED)        
        # serializer = serializer = CarritoSerializer(data = request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        
        #return(lista_retorno)

                #CarritoSerializer.create(carritoData)
                