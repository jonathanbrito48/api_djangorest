from rest_framework import serializers
from .models import lojas

class lojaserializer(serializers.ModelSerializer):
    class Meta:
        model = lojas
        fields = [ 'Loja', 'Endereco', 'Bandeira']
        read_only_fileds = ['id','created_at']