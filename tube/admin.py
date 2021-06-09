from django.contrib import admin
from .models import Main, Favorito, Usuario, Reproductor
# Register your models here.
admin.site.register(Main)
admin.site.register(Favorito)
admin.site.register(Usuario)
admin.site.register(Reproductor)