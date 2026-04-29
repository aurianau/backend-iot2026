from django.contrib import admin
from .models import *

admin.site.register(Microacueducto)
admin.site.register(Tanque)
admin.site.register(Vivienda)
admin.site.register(DispositivoIOT)
admin.site.register(Sensor)
admin.site.register(LecturaNivel)
admin.site.register(Valvula)
admin.site.register(Rol)
admin.site.register(UsuarioRol)
admin.site.register(Recurso)
admin.site.register(RecursoRol)

admin.site.register(EstadoValvula)
admin.site.register(EstadoSistema)
admin.site.register(Alerta)
admin.site.register(ComandoRemoto)
admin.site.register(RespuestaComando)
admin.site.register(AuditoriaSistema)