from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from tube.models import Video
from .serializers import VideoSerializador

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_video(request):
    if request.method == 'GET':
        m = Video.objects.all()
        serializer = VideoSerializador(m, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = VideoSerializador(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
