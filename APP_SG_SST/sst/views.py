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

def listado_usuarios(request):
    usuarios = users.objects.all()

    return render(request, 'sst/listado_usuarios.html', {'lista_usuarios': usuarios})

def formulario_usuarios(request, id):
    roles = rol.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_usuario = users.objects.get(id=id)
        variables_plantilla = {'id':id,'user_name':data_usuario.user_name, 'password':data_usuario.password, 'first_surname':data_usuario.first_surname, 'second_surname':data_usuario.second_surname, 'identity_number':data_usuario.identity_number, 'phone':data_usuario.phone, 'cellphone':data_usuario.cellphone, 'address':data_usuario.address, 'email':data_usuario.email, 'admin_status':data_usuario.admin_status, 'activity_status':data_usuario.activity_status, 'id_rol':data_usuario.id_rol, 'lista_roles':roles , 'action_text':"Actualizar usuario"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'user_name':'', 'password':'', 'first_surname':'', 'second_surname':'', 'identity_number':'', 'phone':'', 'cellphone':'', 'address':'', 'email':'', 'admin_status':'', 'activity_status':'', 'id_rol':'', 'lista_roles':roles , 'action_text':"Agregar usuario"}

    return render(request, 'sst/formulario_usuarios.html', variables_plantilla)

def agregar_usuarios(request):
    if request.POST['id'] == '0':
        print("Nueva")
        nuevo_usuario = users(user_name=request.POST['user_name'], password=request.POST['password'], first_surname=request.POST['first_surname'], second_surname=request.POST['second_surname'], identity_number=request.POST['identity_number'], phone=request.POST['phone'], cellphone=request.POST['cellphone'], address=request.POST['address'], email=request.POST['email'], activity_status=request.POST['activity_status'], id_rol=request.POST['id_rol'])
        nuevo_usuario.save()

    else:
        print("Actualiza")
        data_usuario = users.objects.get(id=request.POST['id'])
        data_usuario.user_name = request.POST['user_name']
        data_usuario.password = request.POST['password']   
        data_usuario.first_surname = request.POST['first_surname']
        data_usuario.second_surname = request.POST['second_surname']
        data_usuario.identity_number = request.POST['identity_number']
        data_usuario.phone = request.POST['phone']
        data_usuario.cellphone = request.POST['cellphone']
        data_usuario.address = request.POST['address']
        data_usuario.email = request.POST['email']
        data_usuario.activity_status = request.POST['activity_status']
        data_usuario.id_rol = request.POST['id_rol']
        data_usuario.save()

    usuarios = users.objects.all()

    return render(request, 'sst/listado_usuarios.html', {'lista_usuarios': usuarios})

# encargado

def listado_encargado(request):
    encargados = users.objects.all()

    return render(request, 'sst/listado_encargado.html', {'lista_encargado': encargados})

def formulario_encargado(request, id):
    roles = rol.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_encargado = users.objects.get(id=id)
        variables_plantilla = {'id':id,'user_name':data_encargado.user_name, 'cedula':data_encargado.cedula, 'nivel_de_estudio':data_encargado.nivel_de_estudio, 'carga_PDF_Diploma':data_encargado.carga_PDF_Diploma,}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'user_name':'', 'password':'', 'first_surname':'', 'second_surname':'', 'identity_number':'', 'phone':'', 'cellphone':'', 'address':'', 'email':'', 'admin_status':'', 'activity_status':'', 'id_rol':'', 'lista_roles':roles , 'action_text':"Agregar usuario"}

    return render(request, 'sst/formulario_usuarios.html', variables_plantilla)

def agregar_usuarios(request):
    if request.POST['id'] == '0':
        print("Nueva")
        nuevo_usuario = users(user_name=request.POST['user_name'], password=request.POST['password'], first_surname=request.POST['first_surname'], second_surname=request.POST['second_surname'], identity_number=request.POST['identity_number'], phone=request.POST['phone'], cellphone=request.POST['cellphone'], address=request.POST['address'], email=request.POST['email'], activity_status=request.POST['activity_status'], id_rol=request.POST['id_rol'])
        nuevo_usuario.save()

    else:
        print("Actualiza")
        data_usuario = users.objects.get(id=request.POST['id'])
        data_usuario.user_name = request.POST['user_name']
        data_usuario.password = request.POST['password']   
        data_usuario.first_surname = request.POST['first_surname']
        data_usuario.second_surname = request.POST['second_surname']
        data_usuario.identity_number = request.POST['identity_number']
        data_usuario.phone = request.POST['phone']
        data_usuario.cellphone = request.POST['cellphone']
        data_usuario.address = request.POST['address']
        data_usuario.email = request.POST['email']
        data_usuario.activity_status = request.POST['activity_status']
        data_usuario.id_rol = request.POST['id_rol']
        data_usuario.save()

    usuarios = users.objects.all()

    return render(request, 'sst/listado_usuarios.html', {'lista_usuarios': usuarios})
