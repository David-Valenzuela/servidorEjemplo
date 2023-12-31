# Generated by Django 4.2.3 on 2023-08-20 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=20)),
                ('apellido_cliente', models.CharField(max_length=100)),
                ('telefono_cliente', models.CharField(max_length=12)),
                ('correo_cliente', models.CharField(max_length=50)),
                ('direc_cliente', models.CharField(max_length=100)),
                ('password_cliente', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id_especie', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_especie', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id_proc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proc', models.CharField(max_length=100)),
                ('precio_proc', models.IntegerField()),
                ('descrip_proc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('rut_vet', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_vet', models.CharField(max_length=20)),
                ('apellido_vet', models.CharField(max_length=50)),
                ('img_vet', models.ImageField(blank=True, null=True, upload_to='static/vet/')),
                ('telefono_vet', models.CharField(max_length=12)),
                ('correo_vet', models.CharField(max_length=50)),
                ('password_vet', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_suc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_suc', models.CharField(max_length=50)),
                ('direc_suc', models.CharField(max_length=100)),
                ('telefono_suc', models.CharField(max_length=12)),
                ('correo_suc', models.CharField(blank=True, max_length=50, null=True)),
                ('comuna', models.ForeignKey(db_column='comuna', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id_raza', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_raza', models.CharField(max_length=50)),
                ('especie_masc', models.ForeignKey(db_column='especie_masc', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.especie')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_masc', models.AutoField(primary_key=True, serialize=False)),
                ('chip_masc', models.CharField(blank=True, max_length=15, null=True)),
                ('nombre_masc', models.CharField(max_length=50)),
                ('sexo_masc', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra'), ('Macho Castrado', 'Macho Castrado'), ('Hembra Esterilizada', 'Hembra Esterilizada')], max_length=50)),
                ('edad_masc', models.CharField(choices=[('Adulto', 'Adulto'), ('Cachorro', 'Cachorro')], max_length=50)),
                ('estatura_masc', models.CharField(choices=[('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')], max_length=30)),
                ('fecha_nac', models.DateField()),
                ('color_masc', models.CharField(max_length=100)),
                ('img_masc', models.ImageField(blank=True, null=True, upload_to='static/mascotas/')),
                ('especie_masc', models.ForeignKey(db_column='especie_masc', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.especie')),
                ('raza_mascota', models.ForeignKey(db_column='raza_mascota', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.raza')),
                ('rut_cliente', models.ForeignKey(db_column='rut_cliente', on_delete=django.db.models.deletion.DO_NOTHING, related_name='mascotas', to='veterinariadb.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioAtencion',
            fields=[
                ('id_hora', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupado', 'Ocupado')], max_length=20)),
                ('rut_cli', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre_cli', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_cli', models.CharField(blank=True, max_length=12, null=True)),
                ('correo_cli', models.CharField(blank=True, max_length=50, null=True)),
                ('motivo', models.CharField(blank=True, max_length=300, null=True)),
                ('rut_vet', models.ForeignKey(db_column='rut_vet', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.veterinario')),
                ('sucursal', models.ForeignKey(db_column='sucursal', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.sucursal')),
            ],
            options={
                'ordering': ['fecha', 'hora'],
            },
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id_hist', models.AutoField(primary_key=True, serialize=False)),
                ('peso_masc', models.FloatField()),
                ('fecha_hist', models.DateField()),
                ('descripcion_hist', models.CharField(blank=True, max_length=300, null=True)),
                ('proxima_aten', models.DateField(blank=True, null=True)),
                ('id_masc', models.ForeignKey(db_column='id_masc', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ficha', to='veterinariadb.mascota')),
                ('procedimiento', models.ForeignKey(db_column='procedimiento', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.procedimiento')),
                ('rut_vet', models.ForeignKey(db_column='rut_vet', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.veterinario')),
            ],
            options={
                'ordering': ['-fecha_hist'],
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.ForeignKey(db_column='comuna', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.comuna'),
        ),
        migrations.CreateModel(
            name='Asistente',
            fields=[
                ('rut_asist', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_asist', models.CharField(max_length=20)),
                ('apellido_asist', models.CharField(max_length=50)),
                ('telefono_asist', models.CharField(max_length=12)),
                ('correo_asist', models.CharField(max_length=50)),
                ('password_asist', models.CharField(max_length=300)),
                ('sucursal', models.ForeignKey(db_column='sucursal', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinariadb.sucursal')),
            ],
        ),
    ]
