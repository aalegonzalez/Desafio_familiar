from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def vista_familiares(request):
    # Abrimos el archivo
    archivo = open(r"C:\Users\ale28\Coder_4470\coder44470\Desafio_familia\MVTagonzalez\MVTagonzalez\templates\plantilla.html")

    # Creamos el objeto plantilla
    plantilla = Template(archivo.read())

    # cerramos el archivo para liberar recursos
    archivo.close()

    listado_familiares = ["Alejandro Gonzalez", "Jose Gonzalez", "Lucia Gonzalez"]

    # Diccionario con datos para la plantilla
    datos = {"Apellido": "Gonzalez", "listado_familiares": listado_familiares }

    # Creamos el contexto
    contexto = Context(datos)

    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    # Retornamos la respuesta
    return HttpResponse(documento)




def vista_familiares2(request):

    # Diccionario con datos para la plantilla
    listado_familiares = ["Alejandro Gonzalez", "Jose Gonzalez", "Lucia Gonzalez"]
    datos = {"Apellido": "Gonzalez", "listado_familiares": listado_familiares }


    plantilla = loader.get_template("plantilla.html")
    documento = plantilla.render(datos)



    return HttpResponse(documento)


