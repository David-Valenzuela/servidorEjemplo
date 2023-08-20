from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets import SucursalViewSet, ComunaViewSet,ClienteViewSet, EspecieViewSet, HorarioAtencionViewSet,FelinoViewSet,CaninoViewSet,AsistenteViewSet, VeterinarioViewSet, DisponibleViewSet,OcupadoViewSet,ProcedimientoViewSet, HistMedicoViewSet, RazaViewSet, MascotaViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
# Comuna
router.register(r'comuna', ComunaViewSet)
# SUCURSAL
router.register(r'sucursal', SucursalViewSet)
# VETERINARIO
router.register(r'veterinario', VeterinarioViewSet)
# ASISTENTE
router.register(r'asistente', AsistenteViewSet)
# HORARIO GENERAL
router.register(r'atencion', HorarioAtencionViewSet)
# HORARIO DISPONIBLE
router.register(r'horario/disponible', DisponibleViewSet, basename='horario/disponible')
# HORARIO OCUPADO
router.register(r'horario/ocupado', OcupadoViewSet, basename='horario/ocupado')
# CLIENTE
router.register(r'cliente', ClienteViewSet)
# ESPECIES MASCOTAS
router.register(r'especie', EspecieViewSet)
# RAZAS MASCOTAS
router.register(r'raza', RazaViewSet)
# Raza Felinos
router.register(r'felino', FelinoViewSet, basename='felino')
# Raza Felinos
router.register(r'canino', CaninoViewSet, basename='canino')
# MASCOTA
router.register(r'mascota', MascotaViewSet)
# PROCEDIMIENTO
router.register(r'procedimiento', ProcedimientoViewSet)
# HISTORIAL MEDICO MASCOTA
router.register(r'historial', HistMedicoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)