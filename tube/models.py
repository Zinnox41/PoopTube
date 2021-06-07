from django.db import models

# Create your models here.
class Main(models.Model):
    id_main = models.IntegerField(primary_key=True, verbose_name='Id de main')
    nombre_main = models.CharField(max_length=40, verbose_name='Nombre del main ')

    def __str__(self):
        return self.nombre_main

class Favorito(models.Model):
    id_favorito = models.IntegerField(primary_key=True, verbose_name='Id de favorito')
    nombrefavorito_video = models.CharField(max_length=40, verbose_name='Nombre del video favorito ')
    main = models.ForeignKey(Main,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_favorito

class Historial(models.Model):
    id_historial = models.IntegerField(primary_key=True, verbose_name='Id de historial')
    nombrehistorial_video = models.CharField(max_length=40, verbose_name='Nombre del video historial')
    main = models.ForeignKey(Main,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_historial

class Reproductor(models.Model):
    id_reproductor = models.IntegerField(primary_key=True, verbose_name='Id de reproductor')
    nombre_video = models.CharField(max_length=40, verbose_name='Nombre del video')
    comentario = models.CharField(max_length=80, verbose_name='comentario')
    main = models.ForeignKey(Main,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_reproductor

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='Id de usuario')
    nombre = models.CharField(max_length=40, verbose_name='Nombre de usuario')
    apellido = models.CharField(max_length=40, verbose_name='apellido de usuario')
    correo = models.CharField(max_length=40, verbose_name='correo de usuario')
    main = models.ForeignKey(Main,on_delete=models.CASCADE)

    def __str__(self):
        return self.id_usuario