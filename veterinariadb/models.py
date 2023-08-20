from django.db import models
# VETERINARIO
class Veterinario(models.Model):
    rut_vet = models.CharField(primary_key=True, max_length=10)
    nombre_vet = models.CharField(max_length=20)
    apellido_vet = models.CharField(max_length=50)
    img_vet = models.ImageField(blank=True, null=True, upload_to='static/vet/')
    telefono_vet = models.CharField(max_length=12)
    correo_vet = models.CharField(max_length=50)
    password_vet = models.CharField(max_length=300)

    def __str__(self):
        return'{} {}'.format(self.nombre_vet, self.apellido_vet)
# COMUNA
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    def __str__(self):
        return'{}'.format(self.nombre_comuna)
# SUCURSAL
class Sucursal(models.Model):
    id_suc = models.AutoField(primary_key=True)
    nombre_suc = models.CharField(max_length=50)
    direc_suc = models.CharField(max_length=100)
    telefono_suc = models.CharField(max_length=12)
    correo_suc = models.CharField(max_length=50, blank=True, null=True)
    comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna')
    def __str__(self):
        return'{}'.format(self.nombre_suc)
# ASISTENTE
class Asistente(models.Model):
    rut_asist = models.CharField(primary_key=True, max_length=10)
    nombre_asist = models.CharField(max_length=20)
    apellido_asist = models.CharField(max_length=50)
    telefono_asist = models.CharField(max_length=12)
    correo_asist = models.CharField(max_length=50)
    password_asist = models.CharField(max_length=300)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='sucursal')

    def __str__(self):
        return'{} {}'.format(self.nombre_asist, self.apellido_asist)
# HORARIO
class HorarioAtencion(models.Model):
    id_hora = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    class Estados(models.TextChoices):
        Disponible = "Disponible"
        Ocupado = "Ocupado"
    estado = models.CharField(max_length=20, choices=Estados.choices)
    rut_cli = models.CharField(max_length=10, blank=True, null=True)
    nombre_cli = models.CharField(max_length=50, blank=True, null=True)
    telefono_cli = models.CharField(max_length=12, blank=True, null=True)
    correo_cli = models.CharField(max_length=50, blank=True, null=True)
    motivo = models.CharField(max_length=300, blank=True, null=True)
    rut_vet = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='rut_vet')
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='sucursal') 
    def __str__(self):
        return'{} - {}'.format(self.fecha, self.hora)

    class Meta:
        ordering = ["fecha","hora"]
# CLIENTE
class Cliente(models.Model):
    rut_cliente = models.CharField(primary_key=True, max_length=10)
    nombre_cliente = models.CharField(max_length=20)
    apellido_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=12)
    correo_cliente = models.CharField(max_length=50)
    direc_cliente = models.CharField(max_length=100)
    password_cliente = models.CharField(max_length=300)
    comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna')
    def __str__(self):
        return'{} {}'.format(self.nombre_cliente, self.apellido_cliente)
# ESPECIE
class Especie(models.Model):
    id_especie = models.AutoField(primary_key=True)
    nombre_especie = models.CharField(max_length=50)

    def __str__(self):
        return'{}'.format(self.nombre_especie)
# RAZA
class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nombre_raza = models.CharField(max_length=50)
    especie_masc = models.ForeignKey(Especie, models.DO_NOTHING, db_column='especie_masc')

    def __str__(self):
        return'{}'.format(self.nombre_raza)
# MASCOTA
class Mascota(models.Model):
    id_masc = models.AutoField(primary_key=True)
    chip_masc = models.CharField(max_length=15, blank=True, null=True)
    nombre_masc = models.CharField(max_length=50)
    class sexo(models.TextChoices):
        Macho = "Macho"
        Hembra = "Hembra"
        Macho_Castrado = "Macho Castrado"
        Hembra_Esterilizada = "Hembra Esterilizada"
    sexo_masc = models.CharField(max_length=50, choices=sexo.choices)
    class edad(models.TextChoices):
        Adulto = "Adulto"
        Cachorro = "Cachorro"
    edad_masc = models.CharField(max_length=50,choices=edad.choices)
    class estatura(models.TextChoices):
        Pequeño = "Pequeño"
        Mediano = "Mediano"
        Grande = "Grande"
    estatura_masc = models.CharField(max_length=30, choices=estatura.choices)
    fecha_nac = models.DateField()
    color_masc = models.CharField(max_length=100)
    img_masc = models.ImageField(blank=True, null=True,upload_to='static/mascotas/')
    rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cliente',related_name="mascotas")
    especie_masc = models.ForeignKey(Especie, models.DO_NOTHING, db_column='especie_masc')
    raza_mascota = models.ForeignKey(Raza, models.DO_NOTHING, db_column='raza_mascota')

    def __str__(self):
        return'{}'.format(self.nombre_masc)
# PROCEDIMIENTO
class Procedimiento(models.Model):
    id_proc = models.AutoField(primary_key=True)
    nombre_proc = models.CharField(max_length=100)
    precio_proc = models.IntegerField()
    descrip_proc = models.CharField(max_length=300)

    def __str__(self):
        return'{}'.format(self.nombre_proc)
    
# HISTORIAL
class HistorialMedico(models.Model):
    id_hist = models.AutoField(primary_key=True)
    peso_masc = models.FloatField()
    fecha_hist = models.DateField()
    descripcion_hist = models.CharField(max_length=300, blank=True, null=True)
    proxima_aten = models.DateField(blank= True, null=True)
    id_masc = models.ForeignKey('Mascota', models.DO_NOTHING, db_column='id_masc',related_name="ficha")
    rut_vet = models.ForeignKey('Veterinario', models.DO_NOTHING, db_column='rut_vet')
    procedimiento = models.ForeignKey('Procedimiento', models.DO_NOTHING, db_column='procedimiento')

    class Meta:
        ordering = ["-fecha_hist"]

