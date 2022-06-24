from ctypes.wintypes import HLOCAL
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader

from Proyecto0.models import Curso

def mostrartxt(request):
    return HttpResponse("Hola Hola")

def fechahoy(request):
    dia = datetime.today()

    documentotxt = f"Hoy es {dia}"

    return HttpResponse(documentotxt)

def fechanac(request,fechanac):
    fechahoy = datetime.today()
    anio =fechahoy.year
   
    fechanac =int(fechanac)

    edad = anio - fechanac

    mostrar = f"Tenes {edad} años"

    return HttpResponse(mostrar)

def pruebaTemplate(self):
    
    curso = Curso(nombre = "Sergio", camada = "10")

    curso.save()
    #nombre = "Sergio"
    #apellido = "Vega"

    #dicc = {"Nombre":nombre, "Apellido":apellido}

    #miHtml = open("C:/Users/USUARIO/Documents/Python/proyecto desde 0/Proyecto0/Proyecto0/documento.html")

    plantilla = loader.get_template('documento.html')

    #miContexto = Context(dicc)

 #   documento = f"El curso es : {curso.nombre}, la camada: {curso.camada}"

    documento = plantilla.render(curso)

    return HttpResponse(documento)

   
# Falta que aparezca la variable en el template