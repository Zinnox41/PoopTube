from django.urls import path
from .views import lista_video,manipular_video



urlpatterns = [
    path('lista_video',lista_video,name="lista_video"),
    path('datos_video/<id>',manipular_video,name="manipular_video"),

]