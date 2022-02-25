from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista
    p1=Persona("Profesor Juan", "Díaz")
    # p1=Persona("Profesor Manuel", "Díaz")
    nombre="Juan"
    apellido="Díaz"
    ahora=datetime.datetime.now()
    temas_del_curso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    # doc_externo=open("/home/mesa20/Documents/tutos/django/proyecto1/proyecto1/templates/my_template.html")
    # tpl=Template(doc_externo.read())
    # doc_externo.close()
    # doc_externo=loader.get_template('my_template.html')
    # ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,
    # "momento_actual":ahora,"temas":temas_del_curso})
    # doc=tpl.render(ctx)
    # doc=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,
    # "momento_actual":ahora,"temas":temas_del_curso})
    # return HttpResponse(doc)
    return render(request, "my_template.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,
    "momento_actual":ahora,"temas":temas_del_curso})

def curso_c(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"curso_c.html",{"get_time":fecha_actual})

def curso_css(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"curso_css.html",{"get_time":fecha_actual})

def despedida(request):
    return HttpResponse("Hasta luego alumnos de django")

def get_time(request):
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>
    """ % fecha_actual
    return HttpResponse(documento)

def calc_age(request,edad,agno):
    # edad_actual=18
    periodo=agno-2019
    # edad_futura=edad_actual+periodo
    edad_futura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s" %(agno,edad_futura)

    return HttpResponse(documento)