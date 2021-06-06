from django.contrib import admin
from django.urls import path, include
from .views import principal


urlpatterns = [
    path('',principal, name="principal")
]
    