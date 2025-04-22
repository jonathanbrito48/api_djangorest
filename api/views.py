from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,mixins,status
from rest_framework.permissions import IsAuthenticated
from .models import integration
from .serializers import IntegrationSerializer
from .authentication import MD5TokenAuthentication


class IntegrationViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = integration.objects.all()
    serializer_class = IntegrationSerializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]
    max_bulk_items = 20000

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # Retorna uma queryset vazia durante a geração do esquema
            return integration.objects.none()
        return integration.objects.filter(empresa=self.request.user)

    def create(self,request, *args, **kwargs):

        if isinstance(request.data, list) and len(request.data) > self.max_bulk_items:
            return Response(
                {
                    "error":f"Máximo de {self.max_bulk_items} itens por request",
                    "enviados": len(request.data)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data,many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    
    def perform_create(self, serializer):

        if isinstance(serializer, list):
            for item in serializer:
                item.save(empresa=self.request.user)
        else:
            serializer.save(empresa=self.request.user)

