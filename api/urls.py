from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LojasViewSet

router = DefaultRouter()
router.register(r'lojas',LojasViewSet,basename='lojas')

urlpatterns = [
    path('',include(router.urls)),
]