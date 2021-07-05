from django.db.models.base import Model
from rest_framework import serializers
from tube.models import Video

class VideoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Video 
        fields = ['id_video','url_vi','nombre_vi','descripcion_vi','publicacion_vi','img_minatura','categoria']