from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from pf_app.models.user import User
from pf_app.serializers.userSerializer import UserSerializer

class UserDataView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args,**kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        validated_data = tokenBackend.decode(token,verify=False)

        if validated_data['ID_Usuario'] != kwargs['pk']:
            stringResponse = {'detail':'No tiene acceso a esta informacion'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request,*args,**kwargs)
        