from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# ============================================================
# VISTA: INICIO
# ============================================================
def inicio(request):
    rol = None
    if request.user.is_authenticated:
        try:
            rol = request.user.perfilusuario.rol.nombre
        except:
            rol = "Sin rol asignado"
            
    contexto = {
        "titulo": "Control de Usuarios",
        "mensaje": "Bienvenido a la Práctica 05 con Django",
        "rol": rol
    }
    return render(request, "usuarios/inicio.html", contexto)

# ============================================================
# VISTA: INICIAR SESIÓN
# ============================================================
def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        usuario = authenticate(request, username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            return redirect("inicio")
            
        contexto = {"error": "Usuario o contraseña incorrectos"}
        return render(request, "usuarios/login.html", contexto)
        
    return render(request, "usuarios/login.html")