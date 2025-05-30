from email.mime import base
from django.contrib import admin
from django.urls import include, path

from core.views.modelo import ModeloViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import AcessorioViewSet, CorViewSet, ModeloViewSet, VeiculoViewSet, UserViewSet

router = DefaultRouter()

router.register(r'acessorios', AcessorioViewSet, basename='acessorios')
router.register(r'cores', CorViewSet, basename='cores')
router.register(r'modelos', ModeloViewSet, basename='modelos')
router.register(r'veiculos', VeiculoViewSet, basename='veiculos')
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
