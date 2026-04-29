from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register('usuario', UsuarioViewSet)
router.register('rol', RolViewSet)
router.register('usuario-rol', UsuarioRolViewSet)

router.register('microacueducto', MicroacueductoViewSet)
router.register('tanque', TanqueViewSet)
router.register('vivienda', ViviendaViewSet)

router.register('dispositivo', DispositivoIOTViewSet)
router.register('sensor', SensorViewSet)
router.register('lectura', LecturaNivelViewSet)
router.register('valvula', ValvulaViewSet)

router.register('estado-valvula', EstadoValvulaViewSet)
router.register('estado-sistema', EstadoSistemaViewSet)
router.register('alerta', AlertaViewSet)
router.register('comando-remoto', ComandoRemotoViewSet)
router.register('respuesta-comando', RespuestaComandoViewSet)
router.register('auditoria', AuditoriaSistemaViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # JWT LOGIN
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]