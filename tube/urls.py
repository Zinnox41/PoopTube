from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import principal, historial, favorito, contactanos, contra, reproductor, listado, lista_categoria,  guardar_video, eliminar_video, modificar, modificar_video, login_view, logout_view, form_login


urlpatterns = [
    path('',principal, name="principal"),
    path('historial', historial, name="historial"),
    path('favorito', favorito, name="favorito"),
    path('contactanos',contactanos, name="contactanos"),
    path('contra', contra, name="contra"),
    path('reproductor', reproductor, name="reproductor"),
    path('listado', listado, name="listado"),
    path('registro_video', lista_categoria, name="registro_video"),
    path('registro', guardar_video, name="registro"),
    path('eliminar/<int:id>',eliminar_video, name="eliminar_video"),
    path('modificar_video/<int:id>',modificar, name="modificar_video"),
    path('modificar',modificar_video, name="modificar"),
    

    path('login/',form_login, name="login"),
    path('sesion/',login_view, name="sesion"),
    path('logout/',logout_view,name="logout"),
    #path('logout/',LogoutView.as_view(template_name='tube/principal.html'),name="logout"),


]