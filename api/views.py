
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.contrib.auth.models import User


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UsuarioRolViewSet(viewsets.ModelViewSet):
    queryset = UsuarioRol.objects.all()
    serializer_class = UsuarioRolSerializer


class MicroacueductoViewSet(viewsets.ModelViewSet):
    queryset = Microacueducto.objects.all()
    serializer_class = MicroacueductoSerializer


class TanqueViewSet(viewsets.ModelViewSet):
    queryset = Tanque.objects.all()
    serializer_class = TanqueSerializer


class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer


class DispositivoIOTViewSet(viewsets.ModelViewSet):
    queryset = DispositivoIOT.objects.all()
    serializer_class = DispositivoIOTSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class LecturaNivelViewSet(viewsets.ModelViewSet):
    queryset = LecturaNivel.objects.all()
    serializer_class = LecturaNivelSerializer


class ValvulaViewSet(viewsets.ModelViewSet):
    queryset = Valvula.objects.all()
    serializer_class = ValvulaSerializer


class EstadoValvulaViewSet(viewsets.ModelViewSet):
    queryset = EstadoValvula.objects.all()
    serializer_class = EstadoValvulaSerializer


class EstadoSistemaViewSet(viewsets.ModelViewSet):
    queryset = EstadoSistema.objects.all()
    serializer_class = EstadoSistemaSerializer


class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer


class ComandoRemotoViewSet(viewsets.ModelViewSet):
    queryset = ComandoRemoto.objects.all()
    serializer_class = ComandoRemotoSerializer


class RespuestaComandoViewSet(viewsets.ModelViewSet):
    queryset = RespuestaComando.objects.all()
    serializer_class = RespuestaComandoSerializer


class AuditoriaSistemaViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaSistema.objects.all()
    serializer_class = AuditoriaSistemaSerializer