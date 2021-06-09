# Generated by Django 3.2.3 on 2021-06-09 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactanos',
            fields=[
                ('id_contactanos', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Contactanos')),
                ('mailpoop', models.CharField(max_length=40, verbose_name='ingrese su correo')),
                ('comentariopoop', models.CharField(max_length=80, verbose_name='comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id_premium', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Premium')),
                ('usuariopoop', models.CharField(max_length=40, verbose_name='Nombre de usuario ')),
                ('mail', models.CharField(max_length=40, verbose_name='correo de usuario')),
                ('contrapoop', models.CharField(max_length=40, verbose_name='contraseña del usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Reproductor',
            fields=[
                ('id_reproductor', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de reproductor')),
                ('nombre_video', models.CharField(max_length=40, verbose_name='Nombre del video')),
                ('comentario', models.CharField(max_length=80, verbose_name='comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de usuario')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre de usuario')),
                ('correo', models.CharField(max_length=40, verbose_name='correo de usuario')),
                ('contra', models.CharField(max_length=40, verbose_name='contraseña del usuario')),
                ('contra2', models.CharField(max_length=40, verbose_name='repetir contraseña del usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id_main', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de main')),
                ('nombre_main', models.CharField(max_length=40, verbose_name='Nombre del main ')),
                ('contactanos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tube.contactanos')),
                ('premium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tube.premium')),
                ('reproductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tube.reproductor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tube.usuario')),
            ],
        ),
    ]