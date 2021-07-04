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

def guardar_video(request):
    n_codigo = request.GET['codigo']
    url_m = request.GET['url']
    nombre_m = request.GET['nombre']
    descripcion_m = request.GET['descripcion']
    categoria_m = request.POST['categoria']
    categoria_m2 = Categoria.objects.get(id_categoria = categoria_m )
    Usuario.objects.create(id_video = n_codigo, url_vi = url_m, nombre_vi = nombre_m, descripcion_vi = descripcion_m, categoria = categoria_m2 )

    messages.success(request,'video Registrado Correctamente')

    return redirect('registro_video')
