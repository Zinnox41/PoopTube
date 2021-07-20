from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])

def login(request):

    data = JSONParser().parse(request)

    u = data['nombre_usu']

    c = data['contra_usu']

    try:

        user = User.objects.get(nombre_usu = u)

    except User.DoesNotExist:

        return Response("Usuario Incorrecto")

    contra_valida = check_password(c,user.contra_usu)

    if not contra_valida:

        return Response("Contraseña Incorrecta")


    token,created = Token.objects.get_or_create(user = user)

    return Response(token.key)