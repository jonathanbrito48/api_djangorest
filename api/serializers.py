from rest_framework import serializers
from .models import dim_cliente

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=dim_cliente
        fields=['id_cliente','nome_cliente','segmento','pais','cidade','estado','codigo_postal',
                'regiao']
        read_only_fields=['id','created_at']