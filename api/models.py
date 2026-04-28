from django.db import models


# MICROACUEDUCTO
class Microacueducto(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=30)
    fecha_registro = models.DateTimeField(auto_now_add=True)


# TANQUE
class Tanque(models.Model):
    microacueducto = models.ForeignKey(Microacueducto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    capacidad_litros = models.FloatField()
    nivel_actual = models.FloatField()
    tipo = models.CharField(max_length=50)


# VIVIENDA
class Vivienda(models.Model):
    microacueducto = models.ForeignKey(Microacueducto, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    estado = models.CharField(max_length=30)


# DISPOSITIVO IOT
class DispositivoIOT(models.Model):
    tanque = models.ForeignKey(Tanque, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    ip = models.CharField(max_length=50)
    fecha_instalacion = models.DateField()


# SENSOR
class Sensor(models.Model):
    dispositivo = models.ForeignKey(DispositivoIOT, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)


# LECTURA NIVEL
class LecturaNivel(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)


# VALVULA
class Valvula(models.Model):
    dispositivo = models.ForeignKey(DispositivoIOT, on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)


# ROL
class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)


# USUARIO ROL
class UsuarioRol(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)


# RECURSO
class Recurso(models.Model):
    nombre = models.CharField(max_length=50)
    url_backend = models.CharField(max_length=100)
    url_frontend = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    icono = models.CharField(max_length=50)
    orden = models.IntegerField()
    recurso_padre = models.CharField(max_length=50, null=True, blank=True)
    estado = models.BooleanField(default=True)


# RECURSO ROL
class RecursoRol(models.Model):
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)