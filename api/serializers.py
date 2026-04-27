from rest_framework import serializers
from .models import (
    Microacueducto,
    Tanque,
    Sensor,
    Valvula,
    Usuario
)

class MicroacueductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microacueducto
        fields = '__all__'


class TanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanque
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class ValvulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valvula
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'