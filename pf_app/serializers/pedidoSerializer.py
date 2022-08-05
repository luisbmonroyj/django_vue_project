from pf_app.models.pedido import Pedido
from rest_framework import serializers
#from pf_app.serializers.userData import UserData

class PedidoSerializer(serializers.ModelSerializer):
    #userData = UserData()
    class Meta:
        model = Pedido
        fields = '__all__'
        #['id_usuario','id_pedido','total','status']

    def create(self,validated_data):
        pedidoInstance = Pedido.objects.create(**validated_data)
        return pedidoInstance
    
    def to_representation(self, object):
        order = Pedido.objects.get(id_pedido=object.id_pedido)
        return {'id_pedido': order.id_pedido,
                'id_usuario': order.id_usuario,
                'total': order.total,
                'status': order.status,
                }
            #    'estado': user.estado
            #    considero que estado no deberia mandarlo, dejarlo como tratamiento interno

            
    