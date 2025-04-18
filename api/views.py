from django.shortcuts import render

from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAuthenticated
from .models import dim_cliente,dim_produto,dim_tempo_entrega,dim_tempo_venda,dim_tipo_entrega,fato_vendas
from .serializers import ClienteSerializer
from .authentication import MD5TokenAuthentication

class ClienteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = dim_cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return dim_cliente.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user)