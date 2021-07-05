from django.contrib import admin
from django.urls import path, include
from .views import principal, historial, favorito, contactanos, crear, ingresar, contra, reproductor, listado, lista_categoria,  guardar_video, eliminar_video, modificar, modificar_video


urlpatterns = [
    path('',principal, name="principal"),
    path('historial', historial, name="historial"),
    path('favorito', favorito, name="favorito"),
    path('contactanos',contactanos, name="contactanos"),
    path('crear', crear, name="crear"),
    path('ingresar', ingresar, name="ingresar"),
    path('contra', contra, name="contra"),
    path('reproductor', reproductor, name="reproductor"),
    path('listado', listado, name="listado"),
    path('registro_video', lista_categoria, name="registro_video"),
    path('registro', guardar_video, name="registro"),
    path('eliminar/<int:id>',eliminar_video, name="eliminar_video"),
    path('modificar_video/<int:id>',modificar, name="modificar_video"),
    path('modificar',modificar_video, name="modificar"),

]