from django.shortcuts import render

from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAuthenticated
from .models import lojas
from .serializers import lojaserializer
from .authentication import MD5TokenAuthentication

class LojasViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = lojas.objects.all()
    serializer_class = lojaserializer
    authentication_classes = [MD5TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return lojas.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)