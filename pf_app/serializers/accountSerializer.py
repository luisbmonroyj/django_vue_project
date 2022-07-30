from dataclasses import field
from pf_app.models.account import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = ['balance', 'lastChangeDate', 'isActive']
    