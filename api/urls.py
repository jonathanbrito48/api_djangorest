from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import IntegrationViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="API de testes"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


router = DefaultRouter()
router.register(r'integration',IntegrationViewSet,basename='integratio')

urlpatterns = [
    path('',include(router.urls)),
    path('swagger/',schema_view.with_ui('swagger',cache_kwargs=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]