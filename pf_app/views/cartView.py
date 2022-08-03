from rest_framework import status,views
from rest_framework.response import Response

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
        lista = carritoData['productos_usuario'] #{'1':'4','3':'6'}

        total = 0
        productos = lista.keys()
        #bota una clase diccionario

        for i in range (len(productos)):
            costo = 0
            productoDB = request.filter(id_producto=productos[i]).first
            costo = productoDB.precio * request.lista(productos[i])	
            Total += costo
        
        pedidoCompleto=pedido.save(total,request.id_usuario,status)

    Pedido.save(total,request.id_usuario,status)
        return id_pedido

        for i in range (len(productos)):
            costo = 0
            productoDB = request.filter(id_producto=productos[i]).first
            costo = productoDB.precio * request.Productos_Usuarios.get(productos[i])	
            carrito.save	(request.id_usuario,id_producto,cantidad,costo,pedidoCompleto.id)

    def save(request.id_usuario,id_producto,cantidad,costo):

                #print(carritoData)
                
                return Response(carritoData, status = status.HTTP_201_CREATED)
    