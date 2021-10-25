from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    print(request.session.get('loggeado', False))
    print(request.session.get('login_error', False))
    if request.session.get('loggeado', False):
        return render(request, 'sst/dashboard.html')
    else:
        return redirect('/login')

def login(request):
    print(request.session.get('loggeado', False))
    print(request.session.get('login_error', False))
    if request.session.get('login_error', False) !='':
        print("Error de login")
        variables_plantilla = {'login_error':request.session.get('login_error','')}
    else:
        variables_plantilla = {'login_error':''}

    return render(request, 'sst/login.html', variables_plantilla)

def acceder(request):
    usuario_existe = users.objects.filter(email=request.POST['email'], password=request.POST['password'])
    
    if usuario_existe.exists():
        # Si existe obtiene el id del usuario en una session
        request.session['loggeado'] = usuario_existe[0].id
        request.session['login_error'] = ""
        return redirect('/')
    else:
        # Si no existe se coloca 0 en la session loggeada
        request.session['loggeado'] = 0
        request.session['login_error'] = "Correo y/o clave invalidos"
        return redirect('/login')

# ROLES

def listado_roles(request):
    roles = rol.objects.all()

    return render(request, 'sst/listado_roles.html', {'lista_roles': roles})

# DOCUMENTACION

def formulario_encargado(request):
    pass

def formulario_configuracion(request):
    pass

def formulario_compromisos(request):
    pass

def listado_aliados(request):
    pass

def formulario_aliados(request):
    pass

def formulario_riesgos(request):
    pass

def formulario_plan_emergencia(request):
    pass

# USUARIOS

