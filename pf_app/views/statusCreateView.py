from rest_framework import status,views
from rest_framework.response import Response
from pf_app.serializers.statusSerializer import StatusSerializer

class StatusCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = StatusSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        statusData = {
            #'id_status':request.data['id_status'],
            'descripcion':request.data['descripcion'],
        }
        
        return Response(statusData, status = status.HTTP_201_CREATED)
    