from django.shortcuts import render, redirect
from .models import Video, Categoria, Usuario,Tipo_usuario, Comentario
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 


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
    foto_m = request.FILES['img_foto']
    categoria_m = request.POST['categoria']
    categoria_m2 = Categoria.objects.get(id_categoria = categoria_m )
    Video.objects.create(id_video = n_codigo, url_vi = url_m, nombre_vi = nombre_m, descripcion_vi = descripcion_m, img_minatura = foto_m, categoria = categoria_m2 )

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
    n_codigo = request.POST['codigo']
    url_m = request.POST['url']
    nombre_m = request.POST['nombre']
    descripcion_m = request.POST['descripcion']
    foto_m = request.FILES['img_foto']
    categoria_m = request.POST['categoria']

    categoria_ob = Categoria.objects.get(id_categoria = categoria_m)

    video_m = Video.objects.get(id_video = n_codigo )
    video_m.url_vi = url_m
    video_m.nombre_vi = nombre_m
    video_m.descripcion_vi = descripcion_m
    video_m.img_minatura = foto_m
    video_m.categoria = categoria_ob
    video_m.save()

    messages.success(request,'video Modificada')
    
    return redirect('listado')

def form_login(request):
    return render(request,'tube/ingresar.html')
    
def login_view(request):
    u = request.POST['username']
    c = request.POST['password']
    user = authenticate(username = u, password = c)

    if user is not None:
        if user.is_active:
            login(request,user)
            messages.success(request,'Login Realizado')
            return redirect('principal')
        else:
            messages.error(request,'Usuario inactivo')
    else:
        messages.error(request,'Usuario o Contraseña incorrecta')
    
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('principal')


def crear_user(request):
    
    nombre_a= request.POST['nombre_usu'] 
    apellido_a= request.POST['apellido_usu']
    correo_a= request.POST['correo_usu']
    contra_a= request.POST['contra']
    ccontra_a= request.POST['ccontra']
    crear_tipo_user= Tipo_usuario.objects.get(nombre_tipo_usu="normales")
    User.objects.create_user(username = correo_a, email = correo_a, password = contra_a)
    Usu=User.objects.get(username = correo_a)
    Usuario.objects.create(nombre_usu = nombre_a, apellido_usu = apellido_a, correo_usu = correo_a, contra_usu = contra_a, tipo_usuario = crear_tipo_user)

def comentario(request):
    descripcion_a= request.POST['descripcion_com']
    Comentario.objects.create(descripcion_com = descripcion_a)
    return redirect('comentario')
