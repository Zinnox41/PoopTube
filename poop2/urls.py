from django.urls import path
from .views import lista_video



urlpatterns = [
    path('lista_video',lista_video,name="lista_video"),

]