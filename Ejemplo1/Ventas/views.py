from django.shortcuts import render, redirect
from .models import Mascota, Raza

# Create your views here.
def inicio(request):

    return render(request,'Ventas/index.html')

def home(request):
    return render(request,'Ventas/home.html')

def mascota(request):
    contexto = {"nombre":"Firulai", "edad":"1 año", "pelo": "Castaño", "imagen":"/static/Ventas/img/pet1.jpeg"}
    return render(request,'Ventas/mascota.html',contexto)

def mascota2(request):
    contexto = {"nombre":"Manchitas", "edad":"3 años", "pelo": "Blanco con negro", "imagen":"/static/Ventas/img/pet2.jpg"}
    return render(request,'Ventas/mascota.html',contexto)

def listado(request):
    mascotas = Mascota.objects.all()
    contexto = {"mascota": mascotas}
    return render(request,"Ventas/ListadoM.html",contexto)

def formulario(request):
    razas = Raza.objects.all()
    contexto = {"raza_m": razas}
    return render(request,"Ventas/agregar.html",contexto)

def registrar_m(request):
    chip = request.POST['chip']
    nombre = request.POST['nombre']
    edad = request.POST['edad']
    color = request.POST['pelo']
    foto = request.FILES['foto']
    raza = request.POST['raza']

    raza2 = Raza.objects.get(idRaza = raza)
    Mascota.objects.create(chip = chip, nombreMascota = nombre, edadMascota = edad, colorPelo = color, 
    foto = foto, raza = raza2)
    return redirect('formulario')