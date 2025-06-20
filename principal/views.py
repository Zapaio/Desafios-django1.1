from django.shortcuts import render
import random
# Create your views here.

from django.http import HttpResponse

def saludar_usuario(request,nombre):
    return HttpResponse(f"Hola {nombre}")

def saludo(request,):
    return HttpResponse("Hola desde django"
    "<br>las rutas para visitar son: /hola/ , /numero/ "
    "<br>Para ingresar al saludo de usuario debe escribir /saludar_usuario/(Su nombre)")

def hola(request,):
    return HttpResponse("Hola mundo")

def numero(request,):
    return HttpResponse(f"A continuacion, un numero aleatorio entre 0 y 100 =  {random.randint(0,100)}")

def inicio(request):
    contexto = {"nombre": "Benjamin"}
    return render(request, "principal/index.html",contexto)

def curriculum(request):
    return render(request,"principal/curriculum.html")

