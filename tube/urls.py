from django.contrib import admin
from django.urls import path, include
from .views import principal, historial, favorito, pooppremium, contactanos, crear, ingresar, contra, reproductor, modificar


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
]
    