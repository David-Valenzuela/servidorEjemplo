from rest_framework import viewsets
from veterinariadb.models import Sucursal, Comuna,Veterinario, Asistente, Cliente, Especie, Mascota, HistorialMedico, HorarioAtencion, Raza, Procedimiento
from .serializer import SucursalSerializer,ComunaSerializer,ClienteSerializer, EspecieSerializer, VeterinarioSerializer, AsistenteSerializer, HorAtencionSerializer,ProcedimientoSerializer,HistMedicoSerializer,RazaSerializer, MascotaSerializer
from datetime import date, timedelta, datetime

class ComunaViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    
class AsistenteViewSet(viewsets.ModelViewSet):
    queryset = Asistente.objects.all()
    serializer_class = AsistenteSerializer

class HorarioAtencionViewSet(viewsets.ModelViewSet):
    fecha_final = datetime.now().date() + timedelta(days=7)
    queryset = HorarioAtencion.objects.filter(fecha__range = (date.today(),fecha_final.strftime("%Y-%m-%d")))
    serializer_class = HorAtencionSerializer

class DisponibleViewSet(viewsets.ModelViewSet):
    fecha_final = datetime.now().date() + timedelta(days=7)
    queryset = HorarioAtencion.objects.filter(estado="Disponible", fecha__range = (date.today(),fecha_final.strftime("%Y-%m-%d")))
    serializer_class = HorAtencionSerializer

class OcupadoViewSet(viewsets.ModelViewSet):
    fecha_final = datetime.now().date() + timedelta(days=7)
    queryset = HorarioAtencion.objects.filter(estado="Ocupado", fecha__range = (date.today(),fecha_final.strftime("%Y-%m-%d")))
    serializer_class = HorAtencionSerializer

class ProcedimientoViewSet(viewsets.ModelViewSet):
    queryset = Procedimiento.objects.all()
    serializer_class = ProcedimientoSerializer

class HistMedicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistMedicoSerializer
class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer

class FelinoViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.filter(especie_masc = 2)
    serializer_class = RazaSerializer

class CaninoViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.filter(especie_masc = 1)
    serializer_class = RazaSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer