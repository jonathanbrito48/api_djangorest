from rest_framework import serializers
from .models import integration

read_only_fields=['id','created_at']

class IntegrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=integration
        exclude=['empresa','created_at','id_venda_item']
        read_only_fields=read_only_fields