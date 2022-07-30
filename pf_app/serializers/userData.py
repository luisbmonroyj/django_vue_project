from pf_app.models.user import User
from rest_framework import serializers

class UserData (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['apellido', 'nombre', 'direccion','telefono']
        