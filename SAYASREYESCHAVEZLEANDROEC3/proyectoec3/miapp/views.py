from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    mensaje="""
        <h1>Universidad Nacional Tecnológica de Lima Sur</h1>
        <h2>EP Ingeniería de Sistemas</h2>
        <h3>Bienvenidos</h3>
    """
    return HttpResponse(mensaje)

def uc3(request):
    mensaje = """
         <h1>Lenguaje de programación III</h1>
        <h2>Evaluación de la Unidad de Competencia 3</h2>
        <h3>Docente: Mg. Flor Elizabeth Cerdán León</h3>
        <h3>Integrantes: </h3>
        <h4>. Leandro Blas Luiggi Anderson</h4>
        <h4>. Chavez Gamarra Jose Carlos</h4>
        <h4>. Sayas de la Vega Piero Gabriel</h4>
        <h4>. Reyes Sánchez Óscar Elias</h4>
        """
    return HttpResponse(mensaje)
def noticia(request):
    mensaje = """
        <h1> Noticia</h1>
        <p>Transportistas de Lima, Callao y regiones no prestarán servicio el lunes 4 de julio por paro

Se trata de transporte de carga, urbano, turístico, de auto colectivo, taxis y mototaxis, entre otros. “Si quieren levantar 
el paro que nos llamen cuando tengan los decretos y resoluciones”, dijo el dirigente Giovanni Diez.El presidente de la Unión 
de Gremios de Transporte Multimodal del Perú (UGTRANM), Giovanni Diez, informó que no suspenderán el paro programado para este 
lunes 4 de julio a menos que el Ejecutivo los convoque para informales que ya tienen los decretos y resoluciones que atienden sus 
demandas.Ha habido una acumulación de demandas que vienen desde el mes de noviembre, que salían 27 puntos del petitorio. El 9 de 
abril se vuelve a sumar una siguiente acta donde se han sumado 7 puntos más haciendo un total de 34. Ninguno de los temas ha sido 
resuelto por el Ejecutivo a pesar de haber firmado actas con nosotros. A la fecha no hemos tenido respuesta, todas estas actas 
firmadas y a la problemática de transporte”, precisó en diálogo a RPP Noticias. Indicó que han estado insistiendo con el Ejecutivo 
enviando cartas no solo al ministro de Transportes, sino también al presidente Pedro Castillo, a fin de llegar a acuerdos y no 
perjudicar a la ciudadanía con una paralización. El día 30 de mayo fue la última reunión que tuvimos con el nuevo ministro de 
Transportes y nos explicaron que era nuevo, entonces cada vez que cambian hay que volver a cero. Le dijimos que no necesitábamos 
más diálogo para ver los temas que ya conocían. Así que les dijimos que si quieren levantar el paro que nos llamen cuando tengan 
los decretos y resoluciones que es la única vía para levantar el paro del 4 de julio”, aseveró.
</p>

        """
    return HttpResponse(mensaje)

# Create your views here.
