from rest_framework import status,views
from rest_framework.response import Response
from pf_app.serializers.pedidoSerializer import PedidoSerializer
from pf_app.serializers.carritoSerializer import CarritoSerializer
from pf_app.serializers.productoSerializer import ProductoSerializer

class CarritoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CarritoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print('ACA VA EL SERIALIZER')
        print(serializer)
        print('ACA ACABA EL SERIALIZER')
        
        carritoData = {
            'id_usuario':request.data['id_usuario'],
            'productos_usuario':{'productos':request.data['productos'],'cantidad':request.data['cantidad'],}
            #'costo':request.data['costo'],
        }
        #{productos_usuario:{'1':'4','3':'6'}
        # id_usuario:1
        #} necesito sacar el diccionario del sefgundo elemento del diccionario 
        
        #lista debe tener las llaves y los valores del segundo elemento de del diccionario carritoData
        lista = carritoData['productos_usuario'] 
        
        #{'1': 4, '2': 8, '3': 12, '4': 16}
        total = 0
        cantidades = lista.values()
        productos_diccionario = lista.keys()
        #bota una clase diccionario
        costos = {}
        for i in productos_diccionario:
            costo = 0
            productoDB = request.filter(id_producto=productos_diccionario[i]).first
            costo = productoDB.precio * request.lista(cantidades[i])
            costos[i] = costo
            total += costo   #### Acá se obtiene el total TOTAL
        
        diccionario_entrega = {
            'total':total,
            'id_usuario':request.id_usuario            
        }
        
        pedidoCompleto=PedidoSerializer.create(diccionario_entrega)
        
        y = {
            'id_pedido':pedidoCompleto.id_pedido,
            'id_usuario':pedidoCompleto.id_usuario,
            'productos': productos_diccionario,
            'cantidad':cantidades,
            'costo':costos
        }
        
        return Response(status = status.HTTP_201_CREATED)

        for i in range (len(productos)):
            costo = 0
            productoDB = request.filter(id_producto=productos[i]).first
            costo = productoDB.precio * request.Productos_Usuarios.get(productos[i])	
            carrito.save	(request.id_usuario,id_producto,cantidad,costo,pedidoCompleto.id)
