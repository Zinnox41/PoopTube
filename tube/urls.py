from django.contrib import admin
from django.urls import path, include
from .views import principal, historial


urlpatterns = [
    path('',principal, name="principal"),
    path('historial', historial, name="historial")
]
    