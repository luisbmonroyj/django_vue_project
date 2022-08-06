from posixpath import split
from tkinter import CENTER
from rest_framework import status,views
from rest_framework.response import Response
#from pf_app.models.carrito import Carrito
from pf_app.serializers.pedidoSerializer import PedidoSerializer
from pf_app.serializers.carritoSerializer import CarritoSerializer
from pf_app.models.producto import Producto
#from pf_app.serializers.productoSerializer import ProductoSerializer

class CarritoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        #serializer = CarritoSerializer(data = request.data) #llama al metodo create de carritoSerializer
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        
        # carritoData = {
        #     'id_usuario':request.data['id_usuario'],
        #     'productos_usuario':{'productos':request.data['productos'],'cantidad':request.data['cantidad'],}
        #     #'costo':request.data['costo'],
        #     }

        
        #posiblemente no lo necesite
        userid = request.data['id_usuario']
        #lista debe tener las llaves y los valores del segundo elemento de del diccionario carritoData
        lista = request.data['productos_usuario']#segun el ejemplo, esta linea es
        #{'1': 4, '2': 8, '3': 12, '4': 16}
        #cantidades = lista.values()#segun el ejemplo, esta linea es
        #[4,8,12,16]
        #productos_diccionario = lista.keys()#segun el ejemplo, esta linea es
        #['1','2','3','4'] que son los id_producto que escogio el cliente
        #NECESITO UNA LISTA QUE ME TRAIGA LOS PRECIOS DE LA TABLA PRODUCTO
        #para calcular el costo(=cantidad*Producto.precio) y sumarlos para hallar total
        #lista = carritoData['productos_usuario'] 
        total = 0
        #cantidades = lista.values()
        #productos_diccionario = lista.keys()
        #bota una clase diccionario
        costos = {}
        variable_luis = Producto.objects.all()
        print(variable_luis)
        print('llegué')
        print(lista)
        #print(productos_diccionario)
        h = 0
        for i in lista:
            # i -> diccionario
            j = i.values()
            k = i.keys()
            print((j))
            print((k))
            for z, l in i.items():
                costo = 0
                productoDB = variable_luis.get(pk=int(z))
                costo = productoDB.precio * l
                costos[h] = costo
                h += 1
                total += costo   #### Acá se obtiene el total TOTAL
        
        print(total)
        print(costos)
        
        
        diccionario_entrega = {
            'total':total,
            'id_usuario':request.id_usuario            
        }
        #en esta linea deberia crearse un pedido en la tabla PEDIDO para poder agregar su id a los datos que van a la tabla carrito
        pedidoCompleto=PedidoSerializer.create(diccionario_entrega)

        # for i in productos_diccionario:
        #     texto = '{\n' + f'"id_usuario":{userid}, \n"productos_usuario": {productos_diccionario[int(i)-1]}, \n"cantidad": {cantidades[int(i)-1]}' + '\n}'
        #     serializer.create(texto)

        for i in productos_diccionario: #productos_diccionario son las llaves de lista, y lista es el diccionario {id_producto:cantidad}
            carritoData = {
                'id_pedido':pedidoCompleto.id_pedido,
                'id_usuario':pedidoCompleto.id_usuario,
                'productos': productos_diccionario[i],
                'cantidad':cantidades[i],
                'costo':costos[i]
            }
            return Response(carritoData,status = status.HTTP_201_CREATED)

        # for i in range (len(productos)):
        #     costo = 0
        #     productoDB = request.filter(id_producto=productos[i]).first
        #     costo = productoDB.precio * request.Productos_Usuarios.get(productos[i])	
        #     carrito.save	(request.id_usuario,id_producto,cantidad,costo,pedidoCompleto.id)
