from rest_framework import serializers
from pf_app.models.account import Account
from pf_app.models.user import User
from pf_app.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer
    class Meta:
        model = User
        fields = ['id', ]