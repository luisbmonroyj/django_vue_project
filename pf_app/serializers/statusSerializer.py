from rest_framework import serializers
from pf_app.models.status import Status
#from pf_app.serializers.userData import UserData

class StatusSerializer(serializers.ModelSerializer):
    #userData = UserData()
    class Meta:
        model = Status
        fields = '__all__'
        #['id_status','descripcion']

    def create(self,validated_data):
        statusInstance = Status.objects.create(**validated_data)
        return statusInstance
    
    def to_representation(self, object):
        status = Status.objects.get(id_status=object.id_status)
        return {'id_status': status.id_status,
                'descripcion': status.descripcion
                }
            
            
    