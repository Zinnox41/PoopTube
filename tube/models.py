from django.db import models



class Premium(models.Model):
    id_premium = models.IntegerField(primary_key=True, verbose_name='Id de Premium')
    usuariopoop= models.CharField(max_length=40, verbose_name='Nombre de usuario ')
    mail = models.CharField(max_length=40, verbose_name='correo de usuario')
    contrapoop = models.CharField(max_length=40, verbose_name='contraseña del usuario')

    def __str__(self):
        return self.usuariopoop


class Reproductor(models.Model):
    id_reproductor = models.IntegerField(primary_key=True, verbose_name='Id de reproductor')
    nombre_video = models.CharField(max_length=40, verbose_name='Nombre del video')
    comentario = models.CharField(max_length=80, verbose_name='comentario')
    

    def __str__(self):
        return self.nombre_video

class Contactanos(models.Model):
    id_contactanos = models.IntegerField(primary_key=True, verbose_name='Id de Contactanos')
    mailpoop = models.CharField(max_length=40, verbose_name='ingrese su correo')
    comentariopoop = models.CharField(max_length=80, verbose_name='comentario')
    

    def __str__(self):
        return self.comentariopoop

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='Id de usuario')
    nombre = models.CharField(max_length=40, verbose_name='Nombre de usuario')
    correo = models.CharField(max_length=40, verbose_name='correo de usuario')
    contra = models.CharField(max_length=40, verbose_name='contraseña del usuario')
    contra2 = models.CharField(max_length=40, verbose_name='repetir contraseña del usuario')


    def __str__(self):
        return self.nombre

class Main(models.Model):
    id_main = models.IntegerField(primary_key=True, verbose_name='Id de main')
    nombre_main = models.CharField(max_length=40, verbose_name='Nombre del main ')
    premium = models.ForeignKey(Premium,on_delete=models.CASCADE)
    reproductor = models.ForeignKey(Reproductor,on_delete=models.CASCADE)
    contactanos = models.ForeignKey(Contactanos,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_main