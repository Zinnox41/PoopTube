from django.shortcuts import render, redirect
from .models import Premium, Reproductor, Contactanos, Usuario, Main
from django.contrib import messages


# Create your views here.
def principal(request):

    return render(request,'tube/principal.html')

def historial(request):
    return render(request, 'tube/historial.html')

def favorito(request):
    return render(request, 'tube/favorito.html')

def pooppremium(request):
    return render(request, 'tube/pooppremium.html')

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

def modificar(request):
    return render(request, 'tube/modificar.html')

def listado(request):
    usuarios = Usuario.objects.all()
    contexto = {"Usuarios": usuarios} 
    return render(request, 'tube/listadoPoop.html',contexto)

def listado_usuario(request):
    usuarios = Usuario.objects.all()
    contexto = {"Usuarios": usuarios} 
    return render(request, 'tube/formulario.html',contexto)

def guardar_usuario(request):
    nombre_m = request.POST['nombre']
    correo_m = request.POST['correo']
    contra_m = request.POST['contra']
    contra2_m = request.POST['contra2']
    Usuario.objects.Create(nombre = nombre_m, correo = correo_m, contra = contra_m, contra2 = contra2_m)
    messages.success(request,'Usuario Registrado Correctamente')

    return redirect('registro_usuario')

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(id_usuario = id) 
    usuario.delete() 
    messages.success(request,'usuario Eliminada')

    return redirect('listado')
def modificar(request, id):
    usuario1 = Usuario.objects.get(id_usuario = id) 
    main1 = Main.objects.all() 
    contexto = {
        "usuario_modificar" : usuario1,
        "main_usuario" : main1
    }

    return render(request,'tube/modificar.html', contexto)

def modificar_usuario(request):
    nombre_m = request.POST['nombre']
    correo_m = request.POST['correo']
    contra_m = request.POST['contra']
    contra2_m = request.POST['contra2']

    usuario_m = Usuario.objects.get(id_usuario = id)
    usuario_m.nombre = nombre_m
    usuario_m.correo = correo_m
    usuario_m.contra = contra_m
    usuario_m.save() 

    messages.success(request,'Usuario Modificada')
    return redirect('listado')
