from django.db import models



class Favorito(models.Model):
    id_favorito = models.IntegerField(primary_key=True, verbose_name='Id de favorito')
    nombrefavorito_video = models.CharField(max_length=40, verbose_name='Nombre del video favorito ')
    

    def __str__(self):
        return self.nombrefavorito_video

class Historial(models.Model):
    id_historial = models.IntegerField(primary_key=True, verbose_name='Id de historial')
    nombrehistorial_video = models.CharField(max_length=40, verbose_name='Nombre del video historial')
    

    def __str__(self):
        return self.nombrehistorial_video

class Reproductor(models.Model):
    id_reproductor = models.IntegerField(primary_key=True, verbose_name='Id de reproductor')
    nombre_video = models.CharField(max_length=40, verbose_name='Nombre del video')
    comentario = models.CharField(max_length=80, verbose_name='comentario')
    

    def __str__(self):
        return self.nombre_video

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='Id de usuario')
    nombre = models.CharField(max_length=40, verbose_name='Nombre de usuario')
    apellido = models.CharField(max_length=40, verbose_name='apellido de usuario')
    correo = models.CharField(max_length=40, verbose_name='correo de usuario')


    def __str__(self):
        return self.nombre

class Main(models.Model):
    id_main = models.IntegerField(primary_key=True, verbose_name='Id de main')
    nombre_main = models.CharField(max_length=40, verbose_name='Nombre del main ')
    favorito = models.ForeignKey(Favorito,on_delete=models.CASCADE)
    historial = models.ForeignKey(Historial,on_delete=models.CASCADE)
    reproductor = models.ForeignKey(Reproductor,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_main