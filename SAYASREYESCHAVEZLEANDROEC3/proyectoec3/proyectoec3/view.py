from datetime import datetime
from django.template import Template,Context
from django.http import HttpResponse
from django.shortcuts  import render 


def PaginaUc3(request):
    nombre= "Lenguaje de programacion III" 
    trabajo= "Evaluacion de la unidad de competencia 3"
    docente= "Mg. Flor Elizabeth Cerdan Leon"
    integrantes=["Leandro", "Sayas","Reyes","Chavez"]
    plantilla=open("C:/Users/PIERO/Desktop/words de escritorio/SAYASREYESCHAVEZLEANDROEC3/SAYASREYESCHAVEZLEANDROEC3/proyectoec3/proyectoec3/plantillas/uc3.html")
    template= Template(plantilla.read())
    plantilla.close()
    contexto= Context({"nombre": nombre,"trabajo": trabajo,"docente":docente, "integrantes":integrantes})
    mostrar=template.render(contexto)
    return HttpResponse(mostrar)
    
