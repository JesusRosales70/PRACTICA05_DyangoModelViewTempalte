from django.shortcuts import render
from .models import Rol

def inicio(request):
    roles = Rol.objects.all()
    contexto = {
        "titulo": "Control de Usuarios",
        "mensaje": "Bienvenido a la Práctica 05 con Django",
        "roles": roles
    }
    return render(request, "usuarios/inicio.html", contexto)