from rest_framework import serializers
from .models import integration

read_only_fields=['id','created_at']

class IntegrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=integration
        exclude=['empresa','created_at','id_venda_item']
        read_only_fields=read_only_fields

    def validate(self,attrs):
        if isinstance(self.initial_data,list) and len(self.initial_data) > 20000:
            raise serializers.ValidationError("Máximo de 20 mil objetos por request")
        return attrs
