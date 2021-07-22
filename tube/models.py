from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    descripcion_cate= models.CharField(max_length=200, verbose_name='descripcion de categoria ')

    def __str__(self):
        return self.descripcion_cate

class Video(models.Model):
    id_video = models.IntegerField(primary_key=True, verbose_name='Id de video')
    url_vi = models.CharField(max_length=200, verbose_name='url ')
    nombre_vi = models.CharField(max_length=200, verbose_name='Nombre del video')
    descripcion_vi = models.CharField(max_length=200, verbose_name='descripcion del video')
    publicacion_vi = models.DateField(auto_now_add=True)
    img_minatura = models.ImageField(upload_to="imagen video", null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_vi

class Tipo_usuario(models.Model):
    id_tipo_usu = models.IntegerField(primary_key=True, verbose_name='Id tipo de usuario')
    nombre_tipo_usu = models.CharField(max_length=80, verbose_name='nombre tipo de usuario ')

    def __str__(self):
        return self.nombre_tipo_usu

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, verbose_name='Id de usuario')
    nombre_usu = models.CharField(max_length=200, verbose_name='nombre tipo de usuario ')
    apellido_usu = models.CharField(max_length=200, verbose_name='apellido de usuario ')
    correo_usu = models.CharField(max_length=200, verbose_name='correo de usuario')
    contra_usu = models.CharField(max_length=200, verbose_name='contraseña de usuario')
    tipo_usuario = models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE)
    user=models.OneToOneField(User, blank=True ,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_usu

class Comentario(models.Model):
    id_comentario = models.IntegerField(primary_key=True, verbose_name='Id de comentario')
    descripcion_com= models.CharField(max_length=200, verbose_name='descripcion de comentario ')
    publicacion_com = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)

    

class Historial(models.Model):
    id_historial = models.IntegerField(primary_key=True, verbose_name='Id de historial')
    visualizar_hi = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)

class Favorito(models.Model):
    id_favorito = models.IntegerField(primary_key=True, verbose_name='Id de favorito')
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    video = models.ForeignKey(Video,on_delete=models.CASCADE)


