from django.shortcuts import render

from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAuthenticated
from .models import empresa,dim_cliente,dim_produto,dim_tempo_entrega,dim_tempo_venda,dim_tipo_entrega,fato_vendas
from .serializers import EmpresaSerializer
from .authentication import MD5TokenAuthentication

class EmpresaViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = empresa.objects.all()
    serializer_class = EmpresaSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return empresa.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)