from django.shortcuts import render
from django.http.response import HttpResponse

from django.shortcuts import render
from django.template.loader import get_template
import datetime


def saludo(request):
    temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
    compas = ["Larra", "Raúl", "Alicia", "Xidro", "Seba"]

    return render(request, "saludo.html", {"nombre_persona": "Juan", "apellido_persona": "Pérez", "fecha_actual": datetime.datetime.now(),"temas" : temas_del_curso, "compas" : compas})


def despedida(request):
    return HttpResponse("Esta es la página de despedida")
