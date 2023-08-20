from rest_framework import serializers
from veterinariadb.models import Sucursal, Veterinario, Comuna,Especie,Asistente, Cliente, Mascota, HistorialMedico, HorarioAtencion, Raza, Procedimiento
# SE DEBE INSTALAR drf-extra-fields
from drf_extra_fields.fields import Base64ImageField
import bcrypt

class ComunaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comuna
        fields = ['url','id_comuna', 'nombre_comuna']

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['url','id_suc', 'nombre_suc', 'direc_suc','telefono_suc', 'correo_suc', 'comuna']

class VeterinarioSerializer(serializers.ModelSerializer):
    # img_vet = Base64ImageField(required = False)
    class Meta:
        model = Veterinario
        fields = ['url','rut_vet','nombre_vet','apellido_vet','img_vet','telefono_vet','correo_vet','password_vet']

    # ENCRIPTAR EN POST
    def create(self, validated_data):
        password = validated_data.pop("password_vet")  # Extrae el valor del password
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        vet = Veterinario(**validated_data)
        vet.password_vet = hashed_pass.decode('utf-8')  # Asigna la contraseña encriptada
        vet.save()
        return vet
    
    # ENCRIPTAR EN PUT
    def update(self, instance, validated_data):
        password = validated_data.pop("password_vet")
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        instance.rut_vet = validated_data.get('rut_vet', instance.rut_vet)
        instance.nombre_vet = validated_data.get('nombre_vet', instance.nombre_vet)
        instance.apellido_vet = validated_data.get('apellido_vet', instance.apellido_vet)
        instance.img_vet = validated_data.get('img_vet', instance.img_vet)
        instance.telefono_vet = validated_data.get('telefono_vet', instance.telefono_vet)
        instance.correo_vet = validated_data.get('correo_vet', instance.correo_vet)
        instance.password_vet = hashed_pass.decode('utf-8')
        instance.save()
        return instance

class AsistenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistente
        fields = ['url','rut_asist','nombre_asist','apellido_asist','telefono_asist','correo_asist','password_asist', 'sucursal']

    # ENCRIPTAR EN POST
    def create(self, validated_data):
        password = validated_data.pop("password_asist")  # Extrae el valor del password
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        asistente = Asistente(**validated_data)
        asistente.password_asist = hashed_pass.decode('utf-8')  # Asigna la contraseña encriptada
        asistente.save()
        return asistente
    
    # ENCRIPTAR EN PUT
    def update(self, instance, validated_data):
        password = validated_data.pop("password_asist")
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        instance.rut_asist = validated_data.get('rut_asist', instance.rut_asist)
        instance.nombre_asist = validated_data.get('nombre_asist', instance.nombre_asist)
        instance.apellido_asist = validated_data.get('apellido_asist', instance.apellido_asist)
        instance.telefono_asist = validated_data.get('telefono_asist', instance.telefono_asist)
        instance.correo_asist = validated_data.get('correo_asist', instance.correo_asist)
        instance.password_asist = hashed_pass.decode('utf-8')
        instance.sucursal = validated_data.get('sucursal', instance.sucursal)

        instance.save()
        return instance

class HorAtencionSerializer(serializers.HyperlinkedModelSerializer):
    fecha = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = HorarioAtencion
        fields = ["url", "id_hora","fecha","hora","estado","rut_cli","nombre_cli","telefono_cli","correo_cli","motivo","rut_vet","sucursal"]

class ProcedimientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Procedimiento
        fields = ['url','id_proc','nombre_proc','precio_proc','descrip_proc']

class HistMedicoSerializer(serializers.HyperlinkedModelSerializer):
    fecha_hist = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = HistorialMedico
        fields = ["url", "id_hist","peso_masc","fecha_hist","descripcion_hist","proxima_aten","id_masc","rut_vet","procedimiento"]

class EspecieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especie
        fields =['url','id_especie', 'nombre_especie']

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields =['url','id_raza','nombre_raza', 'especie_masc']

class MascotaSerializer(serializers.ModelSerializer):
    # img_masc = Base64ImageField(required = False)
    ficha = HistMedicoSerializer(many=True,read_only=True)
    fecha_nac = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = Mascota
        fields = ["url","id_masc","chip_masc",'nombre_masc','edad_masc','especie_masc','sexo_masc','estatura_masc','fecha_nac','color_masc','img_masc','rut_cliente','raza_mascota','ficha']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    mascotas = MascotaSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['url','rut_cliente','nombre_cliente','apellido_cliente','telefono_cliente','correo_cliente','direc_cliente','password_cliente','comuna','mascotas']
    
        # ENCRIPTAR EN POST
    def create(self, validated_data):
        password = validated_data.pop("password_cliente")  # Extrae el valor del password
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cliente = Cliente(**validated_data)
        cliente.password_cliente = hashed_pass.decode('utf-8')  # Asigna la contraseña encriptada
        cliente.save()
        return cliente
    
    # ENCRIPTAR EN PUT
    def update(self, instance, validated_data):
        password = validated_data.pop("password_cliente")
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        instance.rut_cliente = validated_data.get('rut_cliente', instance.rut_cliente)
        instance.nombre_cliente = validated_data.get('nombre_cliente', instance.nombre_cliente)
        instance.apellido_cliente = validated_data.get('apellido_cliente', instance.apellido_cliente)
        instance.telefono_cliente = validated_data.get('telefono_cliente', instance.telefono_cliente)
        instance.correo_cliente = validated_data.get('correo_cliente', instance.correo_cliente)
        instance.direc_cliente = validated_data.get('direc_cliente', instance.direc_cliente)
        instance.password_cliente = hashed_pass.decode('utf-8')
        instance.save()
        return instance