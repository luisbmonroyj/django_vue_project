from pf_app.models.pedido import Pedido
from rest_framework import serializers
from pf_app.serializers.userData import UserData

class PedidoSerializer(serializers.ModelSerializer):
    #userData = UserData()
    class Meta:
        model = Pedido
        fields = '__all__'
        #['id_usuario','password','apellido','nombre','telefono','direccion','estado']

    def create(self,validated_data):
        pedidoInstance = Pedido.objects.create(**validated_data)
        return pedidoInstance
    
    def to_representation(self, object):
        pedido = Pedido.objects.get(id_pedido=object.id_pedido)
        return {'id_pedido': pedido.id_pedido,
                'id_usuario': pedido.id_usuario,
                'total': pedido.total,
                'status': pedido.status,
                }
            #    'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno

            
    