from django.shortcuts import render

def datosTarea(request):

    return render(request, "tareas.html", {})

