from rest_framework import serializers
from .models import dim_cliente,dim_produto,dim_tempo_entrega,dim_tempo_venda,dim_tipo_entrega,fato_vendas

read_only_fields=['id','created_at']

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=dim_cliente
        fields=['id_cliente',
                'nome_cliente',
                'segmento',
                'pais',
                'cidade',
                'estado',
                'codigo_postal',
                'regiao']
        read_only_fields=read_only_fields


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model=dim_produto
        fields=['id_produto',
                'produto',
                'categoria',
                'sub_categoria']
        read_only_fields=read_only_fields


class TempoEntregaSerializer(serializers.ModelSerializer):

    class Meta:
        model=dim_tempo_entrega
        fields=['id_data_entrega',
                'data_entrega',
                'dia_entrega',
                'mes_entrega',
                'ano_entrega']
        read_only_fields=read_only_fields


class TempoVendaSerializer(serializers.ModelSerializer):

    class Meta:
        model=dim_tempo_venda
        fields=['id_data_venda',
                'data_venda',
                'dia_venda',
                'mes_venda',
                'ano_venda']
        read_only_fields=read_only_fields


class TipoEntregaSerializer(serializers.ModelSerializer):

    class Meta:
        model=dim_tipo_entrega
        fields=['id_tipo_entrega',
                'tipo_entrega']
        read_only_fields=read_only_fields


class VendasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=fato_vendas
        fields=['id_venda_item',
                'venda',
                'produto',
                'cliente',
                'data_venda',
                'data_entrega',
                'tipo_entrega',
                'quantidade',
                'venda_valor',
                'desconto',
                'margem']
        read_only_fields=read_only_fields