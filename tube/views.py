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
    return render(request,'tube/formulario.html',contexto)

def guardar_video(request):
    n_codigo = request.POST['codigo']
    url_m = request.POST['url']
    nombre_m = request.POST['nombre']
    descripcion_m = request.POST['descripcion']
    categoria_m = request.POST['categoria']
    categoria_m2 = Categoria.objects.get(id_categoria = categoria_m )
    Usuario.objects.create(id_video = n_codigo, url_vi = url_m, nombre_vi = nombre_m, descripcion_vi = descripcion_m, categoria = categoria_m2 )

    messages.success(request,'video Registrado Correctamente')

    return redirect('registro_video')

def eliminar_video(request, id):
    video = Video.objects.get(id_video = id) #obtengo la mascota a elminar
    video.delete() #elimino el objeto de la BD
    messages.success(request,'Video Eliminada')

    return redirect('listado')

def modificar(request, id):
    video1 = Video.objects.get(id_video = id)
    categoria1 = Categoria.objects.all()

    contexto = {
        "video_modificar" : video1,
        "categorias_video" : categoria1
    }

    return render(request,'tube/formulario_modificar.html', contexto)

def modificar_video(request):
    id_cod = request.POST['codigo']
    url_m = request.POST['url']
    nombre_m = request.POST['nombre']
    descripcion_m = request.POST['descripcion']
    categoria_m = request.POST['categoria']

    categoria_ob = categoria.objects.get(id_categoria = categoria_m)

    video_m = Video.objects.get(id_video = id_cod )
    video_m.url_vi = url_m
    video_m.nombre_vi = nombre_m
    video_m.descripcion_vi = descripcion_m
    video_m.categoria = categoria_ob
    video_m.save()

    messages.success(request,'video Modificada')
    
    return redirect('listado')


