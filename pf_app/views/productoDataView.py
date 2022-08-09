from django.conf import settings
from rest_framework import generics, status
#from rest_framework.response import Response

from pf_app.models.producto import Producto
from pf_app.serializers.productoSerializer import ProductoSerializer

class ProductoDataView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get(self, request, *args,**kwargs):
        return super().get(request,*args,**kwargs)
