from django.http.response import HttpResponse

   def prueba_auth(request):
        return HttpResponse("Esta la página de Auth")

    def prueba_tareas(request):
        return HttpResponse("Esta es la página Tareas")
