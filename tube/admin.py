from django.contrib import admin
from .models import Categoria, Video, Tipo_usuario, Usuario, Comentario, Historial, Favorito

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Video)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Historial)
admin.site.register(Favorito)
