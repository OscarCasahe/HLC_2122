from django.http.response import HttpResponse


def tareas(request):
    return render(request,"tareas.html", {})
    
