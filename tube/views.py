from django.shortcuts import render, redirect
from .models import Video, Categoria
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

def listado(request):
    videos = Video.objects.all()
    contexto = {"Videos": videos}
    
    return render(request, 'tube/listadoVideo.html',contexto)

def lista_categoria(request):
    categorias = Categoria.objects.all()
    contexto = {"categorias_video" : categorias}
    return render(request,'tube/registrovideo.html',contexto)
