from rest_framework import status,views
from rest_framework.response import Response

from pf_app.serializers.carritoSerializer import CarritoSerializer

class CarritoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CarritoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        #print('ACA VA EL SERIALIZER')
        print(serializer)
        serializer.save()
        #print('ACA ACABA EL SERIALIZER')
        carritoData = {
            'id_usuario':request.data['id_usuario'],
            'id_producto':request.data['id_producto'],
            'cantidad':request.data['cantidad'],
            'costo':request.data['costo'],
        }
        print(carritoData)
        
        return Response(carritoData, status = status.HTTP_201_CREATED)
    