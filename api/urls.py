from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MicroViewSet,
    TanqueViewSet,
    SensorViewSet,
    ValvulaViewSet,
    UsuarioViewSet
)

router = DefaultRouter()

router.register('microacueductos', MicroViewSet)
router.register('tanques', TanqueViewSet)
router.register('sensores', SensorViewSet)
router.register('valvulas', ValvulaViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]