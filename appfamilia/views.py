from django.http import HttpResponse
from appfamilia.models import *
from django.template import Template, Context, loader
# Create your views here.


def vista_familiares3(request):

  familiares = listadefamiliares.objects.all()

  lista_familiar = []

  for miembro in familiares:
    lista_familiar.append( miembro.Nombre, miembro.edad, miembro.fecha)
    
  datos = {"apellido": "Gonzalez", "listado_familiares": lista_familiar }

  plantilla = loader.get_template("plantilla.html")
  
  documento = plantilla.render(datos)

  return HttpResponse(documento)



    
  

    