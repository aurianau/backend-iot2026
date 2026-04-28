from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# =====================
# USUARIO (AUTH DJANGO)
# =====================
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# =====================
# ROL
# =====================
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = '__all__'


class MicroacueductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microacueducto
        fields = '__all__'


class TanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanque
        fields = '__all__'


class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = '__all__'


class DispositivoIOTSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispositivoIOT
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class LecturaNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaNivel
        fields = '__all__'


class ValvulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valvula
        fields = '__all__'