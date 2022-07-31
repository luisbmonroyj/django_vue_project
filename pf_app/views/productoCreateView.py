from rest_framework import status,views
from rest_framework.response import Response

from pf_app.serializers.productoSerializer import ProductoSerializer

class ProductoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        productoData = {
            'nombre_producto':request.data['nombre_producto'],
            'presentacion':request.data['presentacion'],
            'precio':request.data['precio'],
        }
        
        return Response(productoData, status = status.HTTP_201_CREATED)
    