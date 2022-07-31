from pf_app.models.user import User
from rest_framework import serializers
from pf_app.serializers.userData import UserData

class UserSerializer(serializers.ModelSerializer):
    #userData = UserData()
    class Meta:
        model = User
        fields = '__all__'
        #['id_usuario','password','apellido','nombre','telefono','direccion','estado']

    def create(self,validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
    
    def to_representation(self, object):
        user = User.objects.get(id_usuario=object.id_usuario)
        return {'usuario': user.usuario,
                'apellido': user.apellido,
                'nombre': user.nombre,
                'correo': user.correo,
                'telefono': user.telefono,
                'direccion': user.direccion,
            }
            #    'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno

            
    