from django.shortcuts import render

from rest_framework import viewsets,mixins
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

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # Retorna uma queryset vazia durante a geração do esquema
            return integration.objects.none()
        return integration.objects.filter(empresa=self.request.user)

    def perform_create(self, serializer):
        serializer.save(empresa=self.request.user)

