from django.shortcuts import render

from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAuthenticated
from .models import dim_cliente,dim_produto,dim_tempo_entrega,dim_tempo_venda,dim_tipo_entrega,fato_vendas
from .serializers import ClienteSerializer,ProdutoSerializer,TempoEntregaSerializer,TempoVendaSerializer,TipoEntregaSerializer,VendasSerializer
from .authentication import MD5TokenAuthentication


class ClienteViewSet(mixins.ListModelMixin,
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

class ProdutoViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = dim_produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return dim_produto.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user)


class TempoEntregaViewSet(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = dim_tempo_entrega.objects.all()
    serializer_class = TempoEntregaSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return dim_tempo_entrega.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user)


class TempoVendaViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = dim_tempo_venda.objects.all()
    serializer_class = TempoVendaSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return dim_tempo_venda.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user)


class TipoEntregaViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = dim_tipo_entrega.objects.all()
    serializer_class = TipoEntregaSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return dim_tipo_entrega.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user) 


class VendaViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = fato_vendas.objects.all()
    serializer_class = VendasSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return fato_vendas.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user)       