from rest_framework import serializers
from .models import empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = ['client_name','api_token','ativo']
        read_only_fileds = ['id','created_at']