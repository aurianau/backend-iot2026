from rest_framework import viewsets
from .models import *
from .serializers import *

class MicroViewSet(viewsets.ModelViewSet):
    queryset = Microacueducto.objects.all()
    serializer_class = MicroacueductoSerializer


class TanqueViewSet(viewsets.ModelViewSet):
    queryset = Tanque.objects.all()
    serializer_class = TanqueSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ValvulaViewSet(viewsets.ModelViewSet):
    queryset = Valvula.objects.all()
    serializer_class = ValvulaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer