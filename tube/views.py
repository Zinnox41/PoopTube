from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def principal(request):

    return render(request,'tube/principal.html')

def historial(request):
    return render(request, 'tube/historial.html')

def favorito(request):
    return render(request, 'tube/favorito.html')

def contactanos(request):
    return render(request, 'tube/contactanos.html')

def crear(request):
    return render(request, 'tube/crear.html')

def ingresar(request):
    return render(request, 'tube/ingresar.html')

def contra(request):
    return render(request, 'tube/contra.html')

def reproductor(request):
    return render(request, 'tube/reproductor.html')
