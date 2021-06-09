from django.contrib import admin
from django.urls import path, include
from .views import principal, historial, favorito, pooppremium, contactanos, crear, ingresar, contra, reproductor, modificar, listado, listado_usuario, eliminar_usuario, modificar_usuario


urlpatterns = [
    path('',principal, name="principal"),
    path('historial', historial, name="historial"),
    path('favorito', favorito, name="favorito"),
    path('pooppremium', pooppremium, name="pooppremium"),
    path('contactanos',contactanos, name="contactanos"),
    path('crear', crear, name="crear"),
    path('ingresar', ingresar, name="ingresar"),
    path('contra', contra, name="contra"),
    path('reproductor', reproductor, name="reproductor"),
    path('modificar', modificar, name="modificar"),
    path('listado',listado,name="listado"),
    path('registro_usuario',listado_usuario,name="registro_usuario"),
    path('eliminar/<int:id>',eliminar_usuario,name="eliminar_usuario"),
    path('modificar_usuario/<int:id>', modificar, name="modificar_usuario"),
    path('modificar',modificar_usuario,name="modificar"),

]