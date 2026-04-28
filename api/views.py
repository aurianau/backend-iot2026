
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


# =====================
# MICROACUEDUCTO
# =====================
class MicroacueductoViewSet(viewsets.ModelViewSet):
    queryset = Microacueducto.objects.all()
    serializer_class = MicroacueductoSerializer


# =====================
# TANQUE
# =====================
class TanqueViewSet(viewsets.ModelViewSet):
    queryset = Tanque.objects.all()
    serializer_class = TanqueSerializer


# =====================
# VIVIENDA
# =====================
class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer


# =====================
# DISPOSITIVO IOT
# =====================
class DispositivoIOTViewSet(viewsets.ModelViewSet):
    queryset = DispositivoIOT.objects.all()
    serializer_class = DispositivoIOTSerializer


# =====================
# SENSOR
# =====================
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# =====================
# LECTURA NIVEL
# =====================
class LecturaNivelViewSet(viewsets.ModelViewSet):
    queryset = LecturaNivel.objects.all()
    serializer_class = LecturaNivelSerializer


# =====================
# VALVULA
# =====================
class ValvulaViewSet(viewsets.ModelViewSet):
    queryset = Valvula.objects.all()
    serializer_class = ValvulaSerializer