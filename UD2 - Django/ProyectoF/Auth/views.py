from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template


def login(request):

    return render(request, "login.html", {})


