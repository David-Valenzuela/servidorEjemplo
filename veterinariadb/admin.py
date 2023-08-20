from django.contrib import admin

from .models import Veterinario, Sucursal, Comuna,Especie,Asistente, HorarioAtencion, Cliente, Raza, Mascota, Procedimiento, HistorialMedico

admin.site.register(Veterinario)
admin.site.register(Comuna)
admin.site.register(Sucursal)
admin.site.register(Asistente)
admin.site.register(HorarioAtencion)
admin.site.register(Cliente)
admin.site.register(Raza)
admin.site.register(Especie)
admin.site.register(Mascota)
admin.site.register(Procedimiento)
admin.site.register(HistorialMedico)