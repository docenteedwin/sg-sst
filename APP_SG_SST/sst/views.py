from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *
from datetime import date
from .utils import render_to_pdf
from django.views.generic import View
from django.http import HttpResponse
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

def logout(request):
    request.session['loggeado'] = 0
    del request.session['login_error']
    return redirect('/login')

# DOCUMENTACION

# RIESGOS Y EMERGENCIA
def listado_riesgos(request):
    risk_emergency = riesgos_emergencia.objects.all()
    return render(request, 'sst/listado_riesgos.html', {'lista_riskEmergency':risk_emergency})

def formulario_riesgos(request,id):
    risk_emergency = riesgos_emergencia.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_riskEmergency = riesgos_emergencia.objects.get(id=id)
        variables_plantilla = {'id':id,'riesgosFile':data_riskEmergency.riesgosFile, 'emergenciaFile':data_riskEmergency.emergenciaFile, 'lista_riskEmergencys':risk_emergency, 'action_text':"Actualizar riesgos"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'riesgosFile':'', 'emergenciaFile':'', 'lista_riskEmergencys':risk_emergency, 'action_text':"Agregar riesgos"}

    return render(request,'sst/formulario_riesgos.html', variables_plantilla)

def agregar_riesgos(request):
    if request.POST['id'] == '0':
        print("Nueva")

        # CARGA DE ARCHIVOS
        if request.FILES['riesgosFile']:
            riesgos_file = request.FILES['riesgosFile']
            fs = FileSystemStorage()
            filename = fs.save(riesgos_file.name, riesgos_file)
            uploaded_file_url_riesgos = fs.url(filename)

        if request.FILES['emergenciaFile']:
            emergencia_file = request.FILES['emergenciaFile']
            fs = FileSystemStorage()
            filename = fs.save(emergencia_file.name, emergencia_file)
            uploaded_file_url_emergencia = fs.url(filename)

        nuevo_riskEmergency = riesgos_emergencia(riesgosFile=uploaded_file_url_riesgos, emergenciaFile=uploaded_file_url_emergencia)
        nuevo_riskEmergency.save()

    else:
        print("Actualiza")
        data_riskEmergency = riesgos_emergencia.objects.get(id=request.POST['id'])

        riesgos_file = request.FILES['riesgosFile']
        fs = FileSystemStorage()
        filename = fs.save(riesgos_file.name, riesgos_file)
        uploaded_file_url_riesgos = fs.url(filename)

        emergencia_file = request.FILES['emergenciaFile']
        fs = FileSystemStorage()
        filename = fs.save(emergencia_file.name, emergencia_file)
        uploaded_file_url_emergencia = fs.url(filename)

        data_riskEmergency.riesgosFile = request.POST['riesgosFile']
        data_riskEmergency.emergenciaFile = request.POST['emergenciaFile']
        data_riskEmergency.save()

    riskEmergencys = riesgos_emergencia.objects.all()

    return redirect('/riesgos')

# EMPRESA
def listado_empresa(request):
    Empresa = empresa.objects.all()

    return render(request, 'sst/listado_empresa.html', {'lista_empresas': Empresa})

def formulario_empresa(request, id):
    if id !=0 : 
        print ("Actualizar registro")
        data_empresa = empresa.objects.get(id=id)
        variables_plantilla = {'id':id,'nombre_empresa':data_empresa.nombre_empresa, 'nit':data_empresa.nit, 'georreferencia':data_empresa.georreferencia, 'actividad_economica':data_empresa.actividad_economica, 'nivel_riesgo':data_empresa.nivel_riesgo, 'cant_trabajadores':data_empresa.cant_trabajadores, 'naturaleza_juridica':data_empresa.naturaleza_juridica, 'telefono_contacto':data_empresa.telefono_contacto, 'email_contacto':data_empresa.email_contacto, 'tipo_empresa':data_empresa.tipo_empresa, 'action_text':"Actualizar empresa"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'nombre_empresa':'', 'nit':'', 'georreferencia':'', 'actividad_economica':'', 'nivel_riesgo':'', 'cant_trabajadores':'', 'naturaleza_juridica':'', 'telefono_contacto':'', 'email_contacto':'', 'tipo_empresa':'', 'action_text':"Agregar empresa"}

    return render(request, 'sst/formulario_empresa.html', variables_plantilla)

def agregar_empresa(request):
    if request.POST['id'] == '0':
        print("Nueva")
        nueva_empresa = empresa(nombre_empresa=request.POST['nombre_empresa'], nit=request.POST['nit'], georreferencia=request.POST['georreferencia'], actividad_economica=request.POST['actividad_economica'], nivel_riesgo=request.POST['nivel_riesgo'], cant_trabajadores=request.POST['cant_trabajadores'], naturaleza_juridica=request.POST['naturaleza_juridica'], telefono_contacto=request.POST['telefono_contacto'], email_contacto=request.POST['email_contacto'], tipo_empresa=request.POST['tipo_empresa'])
        nueva_empresa.save()

    else:
        print("Actualiza")
        data_empresa = empresa.objects.get(id=request.POST['id'])
        data_empresa.nombre_empresa = request.POST['nombre_empresa']
        data_empresa.nit = request.POST['nit']   
        data_empresa.georreferencia = request.POST['georreferencia']
        data_empresa.actividad_economica = request.POST['actividad_economica']
        data_empresa.nivel_riesgo = request.POST['nivel_riesgo']
        data_empresa.cant_trabajadores = request.POST['cant_trabajadores']
        data_empresa.naturaleza_juridica = request.POST['naturaleza_juridica']
        data_empresa.telefono_contacto = request.POST['telefono_contacto']
        data_empresa.email_contacto = request.POST['email_contacto']
        data_empresa.tipo_empresa = request.POST['tipo_empresa']
        data_empresa.save()

    Empresa = empresa.objects.all()

    return render(request, 'sst/listado_empresa.html', {'lista_empresas': Empresa})

def eliminar_empresa(request, id):
    data_empresa = empresa.objects.get(id=id)
    data_empresa.delete()

    return redirect('/lista_empresa')

def formulario_compromisos(request):
    pass

# ALIADOS
def listado_aliados(request):
    aliados = aliado.objects.all()

    return render(request, 'sst/listado_aliados.html', {'lista_aliados':aliados})

def formulario_aliados(request, id):
        aliados = aliado.objects.all()
        productos = producto_aliado.objects.all().filter(aliado=id)
        
        if id !=0 : 
            print ("Actualizar registro")
            data_aliado = aliado.objects.get(id=id)
            variables_plantilla = {'id':id,'name':data_aliado.name, 'nit':data_aliado.nit, 'arl':data_aliado.arl, 'pago_seguridad_social':data_aliado.pago_seguridad_social, 'seguridad_producto':data_aliado.seguridad_producto, 'cumplimiento_arl':data_aliado.cumplimiento_arl,'lista_aliados':aliados ,'lista_productos':productos ,'action_text':"Actualizar usuario"}

        else:
            print ("Nuevo registro")
            variables_plantilla = {'id':0,'name':'', 'nit':'', 'arl':'', 'pago_seguridad_social':'', 'seguridad_producto':'', 'cumplimiento_arl':'', 'lista_aliados':aliados , 'action_text':"Agregar usuario"}

        return render(request, 'sst/formulario_aliados.html', variables_plantilla)

def agregar_aliados(request):
    if request.POST['id'] == '0':
        print("Nueva")

        # CARGA DE ARCHIVOS
        if request.FILES['arl']:
            arl_file = request.FILES['arl']
            fs = FileSystemStorage()
            filename = fs.save(arl_file.name, arl_file)
            uploaded_file_url_arl = fs.url(filename)

        if request.FILES['cumplimiento_arl']:
            cumplimiento_file = request.FILES['cumplimiento_arl']
            fs = FileSystemStorage()
            filename = fs.save(cumplimiento_file.name, cumplimiento_file)
            uploaded_file_url_cumplimiento = fs.url(filename)

        if request.FILES['pago_seguridad_social']:
            pago_file = request.FILES['pago_seguridad_social']
            fs = FileSystemStorage()
            filename = fs.save(pago_file.name, pago_file)
            uploaded_file_url_pago = fs.url(filename)

        nuevo_aliado = aliado(name=request.POST['name'], nit=request.POST['nit'], arl=uploaded_file_url_arl, cumplimiento_arl=uploaded_file_url_cumplimiento, pago_seguridad_social=uploaded_file_url_pago)
        nuevo_aliado.save()

    else:
        print("Actualiza")
        data_aliado = aliado.objects.get(id=request.POST['id'])

        arl_file = request.FILES['arl']
        fs = FileSystemStorage()
        filename = fs.save(arl_file.name, arl_file)
        uploaded_file_url_arl = fs.url(filename)

        cumplimiento_file = request.FILES['cumplimiento_arl']
        fs = FileSystemStorage()
        filename = fs.save(cumplimiento_file.name, cumplimiento_file)
        uploaded_file_url_cumplimiento = fs.url(filename)

        pago_file = request.FILES['pago_seguridad_social']
        fs = FileSystemStorage()
        filename = fs.save(pago_file.name, pago_file)
        uploaded_file_url_pago = fs.url(filename)

        data_aliado.name = request.POST['name']
        data_aliado.nit = request.POST['nit']   
        data_aliado.arl = request.POST['arl']
        data_aliado.pago_seguridad_social = request.POST['pago_seguridad_social']
        data_aliado.seguridad_producto = request.POST['seguridad_producto']
        data_aliado.cumplimiento_arl = request.POST['cumplimiento_arl']
        data_aliado.save()
        

    aliados = aliado.objects.all()

    return redirect('/aliados')

def eliminar_aliados(request, id):
    data_aliado = aliado.objects.get(id=id)
    producto_aliado.objects.filter(aliado=id).delete()
    data_aliado.delete()

    return redirect('/aliados')

def formulario_productos(request,id, aliado):
    productos = producto_aliado.objects.all()
    print(productos)
    if id !=0 : 
        print ("Actualizar registro")
        data_producto = producto_aliado.objects.get(id=id)
        variables_plantilla = {'id':id,'aliado':aliado, 'nombre':data_producto.nombre, 'seguridad_producto':data_producto.seguridad_producto, 'lista_productos':productos , 'action_text':"Actualizar producto"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'aliado':aliado, 'nombre':'', 'seguridad_producto':'', 'lista_productos':productos , 'action_text':"Agregar producto"}

    return render(request, 'sst/formulario_productos.html', variables_plantilla)
    
def agregar_productos(request):
    if request.POST['id'] == '0':
        print("Nueva")

        # CARGA DE ARCHIVOS
        if request.FILES['seguridad_producto']:
            seguridad_producto_file = request.FILES['seguridad_producto']
            fs = FileSystemStorage()
            filename = fs.save(seguridad_producto_file.name, seguridad_producto_file)
            uploaded_file_url_seguridad_producto = fs.url(filename)
                        
        nuevo_producto = producto_aliado(aliado=request.POST['aliado'], nombre=request.POST['nombre'], seguridad_producto=uploaded_file_url_seguridad_producto)
        nuevo_producto.save()

    else:
        print("Actualiza")
        data_producto = producto_aliado.objects.get(id=request.POST['id'])

        arl_file = request.FILES['arl']
        fs = FileSystemStorage()
        filename = fs.save(arl_file.name, arl_file)
        uploaded_file_url_seguridad_producto = fs.url(filename)

        data_producto.aliado = request.POST['aliado']
        data_producto.nombre = request.POST['nombre']   
        data_producto.uploaded_file_url_seguridad_producto = request.POST['uploaded_file_url_seguridad_producto']
        data_producto.save()
        

    productos = producto_aliado.objects.all()

    return redirect('/formulario_aliados/'+request.POST['aliado'])

def eliminar_productos(request, id):
    data_producto = producto_aliado.objects.get(id=id)
    data_producto.delete()
    
    return redirect('/aliados')

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

    return redirect('/usuarios')

def eliminar_usuarios(request ,id):
    data_usuario = users.objects.get(id=id)
    data_usuario.delete()

    return redirect('/usuarios')

# ENCARGADO

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

def agregar_encargado(request):
    pass

#POLITICAS SG-SST

def formulario_politicas(request,id):
    if id !=0 : 
        politica = Politicas.objects.get(id=id)
        fechaFormat = date.isoformat(politica.fecha)
        variables_plantilla = {'id':id,'empresa':politica.empresa, 'nit':politica.nit, 'compromisos':politica.compromisos, 'requisitos_legales':politica.requisitos_legales, 'objetivos':politica.objetivos, 'comentarios':politica.comentarios, 'firma':politica.firma, 'fecha':fechaFormat}
    else:
        variables_plantilla = {'id':0,'empresa':'', 'nit':'', 'compromisos':'', 'requisitos_legales':'', 'objetivos':'', 'comentarios':'', 'firma':'', 'fecha':''}

    return render(request, 'sst/formulario_politicas.html', variables_plantilla)

def agregar_politicas(request):
    if request.POST['id'] == '0':
        politicas = Politicas(empresa=request.POST['empresa'], nit=request.POST['nit'], compromisos=request.POST['compromisos'], requisitos_legales=request.POST['requisitos_legales'], objetivos=request.POST['objetivos'], comentarios=request.POST['comentarios'], firma=request.POST['firma'], fecha=request.POST['fecha'])
        politicas.save()

    else:
        politicas = Politicas.objects.get(id=request.POST['id'])
        politicas.empresa = request.POST['empresa']
        politicas.nit = request.POST['nit']   
        politicas.compromisos = request.POST['compromisos']
        politicas.requisitos_legales = request.POST['requisitos_legales']
        politicas.objetivos = request.POST['objetivos']
        politicas.comentarios = request.POST['comentarios']
        politicas.firma = request.POST['firma']
        politicas.fecha = request.POST['fecha']
        politicas.save()

    plts = Politicas.objects.all()
    return render(request, 'sst/politicas.html', {'politicas': plts})

def eliminar_politicas(request, id):
    politica = Politicas.objects.filter(id=id).delete()
    plts = Politicas.objects.all()
    return render(request, 'sst/politicas.html', {'politicas': plts})

def ver_politicas(request):
    plts = Politicas.objects.all()
    return render(request, 'sst/politicas.html', {'politicas': plts})

def pdf_politicas(request, id,*args, **kwargs):
    plts = Politicas.objects.get(id=id)
    data = {
            'empresa': plts.empresa,
            'nit': plts.nit,
            'compromisos': plts.compromisos,
            'requisitos_legales': plts.requisitos_legales,
            'objetivos': plts.objetivos,
            'comentarios': plts.comentarios,
            'firma': plts.firma,
            'fecha': plts.fecha
            }
    pdf = render_to_pdf('sst/pdf_politicas.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
    #return render(request, 'sst/pdf_politicas.html', {'politicas': plts})

# MODULO COMITES

# COPASST
def listado_copasst(request):
    miembros = copasst.objects.all()

    return render(request, 'sst/copasst/listado_COPASST.html', {'lista_miembros': miembros})

def formulario_copasst(request, id):
    miembros = copasst.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_miembro = copasst.objects.get(id=id)
        variables_plantilla = {'id':id,'nombre':data_miembro.nombre, 'apellido':data_miembro.apellido, 'cedula':data_miembro.cedula, 'email':data_miembro.email, 'telefono':data_miembro.telefono, 'cargo':data_miembro.cargo, 'lista_miembros':miembros , 'action_text':"Actualizar miembro"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'nombre':'', 'apellido':'', 'cedula':'', 'email':'', 'telefono':'', 'cargo':'', 'lista_miembros':miembros , 'action_text':"Agregar miembro"}

    return render(request, 'sst/copasst/formulario_COPASST.html', variables_plantilla)

def agregar_copasst(request):
    if request.POST['id'] == '0':
        print("Nueva")
        nuevo_miembro = copasst(nombre=request.POST['nombre'], apellido=request.POST['apellido'], cedula=request.POST['cedula'], email=request.POST['email'], telefono=request.POST['telefono'], cargo=request.POST['cargo'])
        nuevo_miembro.save()

    else:
        print("Actualiza")
        data_miembro = copasst.objects.get(id=request.POST['id'])
        data_miembro.nombre = request.POST['nombre']
        data_miembro.apellido = request.POST['apellido']   
        data_miembro.cedula = request.POST['cedula']
        data_miembro.email = request.POST['email']
        data_miembro.telefono = request.POST['telefono']
        data_miembro.cargo = request.POST['cargo']
        data_miembro.save()

    miembros = copasst.objects.all()

    return redirect('/copasst')

def eliminar_copasst(request ,id):
    data_miembro = copasst.objects.get(id=id)
    data_miembro.delete()

    return redirect('/copasst')

def listado_plan_copasst(request):
    planes = plan_copasst.objects.all()

    return render(request, 'sst/copasst/listado_plan_COPASST.html', {'lista_planes': planes})

def formulario_plan_copasst(request, id):
    planes = plan_copasst.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_plan = plan_copasst.objects.get(id=id)
        variables_plantilla = {'id':id,'nombre':data_plan.nombre, 'fecha':data_plan.fecha, 'descripcion':data_plan.descripcion, 'lista_planes':planes , 'action_text':"Actualizar plan"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'nombre':'', 'fecha':'', 'descripcion':'', 'lista_planes':planes , 'action_text':"Agregar plan"}

    return render(request, 'sst/copasst/formulario_plan_COPASST.html', variables_plantilla)

def agregar_plan_copasst(request):
    if request.POST['id'] == '0':
        print("Nueva")
        nuevo_plan = plan_copasst(nombre=request.POST['nombre'], fecha=request.POST['fecha'], descripcion=request.POST['descripcion'])
        nuevo_plan.save()

    else:
        print("Actualiza")
        data_plan = plan_copasst.objects.get(id=request.POST['id'])
        data_plan.nombre = request.POST['nombre']
        data_plan.fecha = request.POST['fecha']   
        data_plan.descripcion = request.POST['descripcion']

        data_plan.save()

    planes = plan_copasst.objects.all()

    return redirect('/plan_copasst')

def eliminar_plan_copasst(request, id):
    data_plan = plan_copasst.objects.get(id=id)
    data_plan.delete()

    return redirect('/plan_copasst')

def listado_votacion_copasst(request):
    votos = archivos_copasst.objects.all().filter(tipo_archivo=0)

    return render(request, 'sst/copasst/listado_votacion_COPASST.html', {'lista_votos': votos})

def formulario_votacion_copasst(request, id):
    votos = archivos_copasst.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_votos = archivos_copasst.objects.get(id=id)
        variables_plantilla = {'id':id, 'votacion':data_votos.votacion, 'tipo_archivo':data_votos.tipo_archivo,'fecha':data_votos.fecha, 'lista_votos':votos , 'action_text':"Actualizar votacion"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0, 'votacion':'', 'tipo_archivo':'', 'fecha':'', 'lista_votos':votos , 'action_text':"Agregar votacion"}

    return render(request, 'sst/copasst/formulario_votacion_COPASST.html', variables_plantilla)
    
def agregar_votacion_copasst(request):
    if request.POST['id'] == '0':
        print("Nueva")

        if request.FILES['votacion']:
            votacion_file = request.FILES['votacion']
            fs = FileSystemStorage()
            filename = fs.save(votacion_file.name, votacion_file)
            uploaded_file_url_votacion = fs.url(filename)
                        
        print(request.POST)
        nueva_votacion = archivos_copasst(tipo_archivo=request.POST['tipo_archivo'], fecha=request.POST['fecha'], votacion=uploaded_file_url_votacion)
        nueva_votacion.save()

    votacion = archivos_copasst.objects.all()

    return redirect('/votacion_copasst')

def eliminar_votacion_copasst(request, id):
    data_votacion = archivos_copasst.objects.get(id=id)
    data_votacion.delete()
    
    return redirect('/votacion_copasst')

def listado_nombramiento_copasst(request):
    nombres = archivos_copasst.objects.all().filter(tipo_archivo=1)

    return render(request, 'sst/copasst/listado_nombramiento_COPASST.html', {'lista_nombres': nombres})

def formulario_nombramiento_copasst(request, id):
    nombres = archivos_copasst.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_nombres = archivos_copasst.objects.get(id=id)
        variables_plantilla = {'id':id, 'votacion':data_nombres.votacion, 'tipo_archivo':data_nombres.tipo_archivo, 'fecha':data_nombres.fecha, 'lista_nombres':nombres , 'action_text':"Actualizar votacion"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0, 'votacion':'', 'tipo_archivo':'', 'fecha':'', 'lista_nombres':nombres , 'action_text':"Agregar votacion"}

    return render(request, 'sst/copasst/formulario_nombramiento_COPASST.html', variables_plantilla)
    
def agregar_nombramiento_copasst(request):
    if request.POST['id'] == '0':
        print("Nueva")

        if request.FILES['nombramiento']:
            nombramiento_file = request.FILES['nombramiento']
            fs = FileSystemStorage()
            filename = fs.save(nombramiento_file.name, nombramiento_file)
            uploaded_file_url_nombramiento = fs.url(filename)
                        
        print(request.POST)
        nueva_nombramiento = archivos_copasst(tipo_archivo=request.POST['tipo_archivo'], fecha=request.POST['fecha'], nombramiento=uploaded_file_url_nombramiento)
        nueva_nombramiento.save()

    nombramiento = archivos_copasst.objects.all()

    return redirect('/nombramiento_copasst')

def eliminar_nombramiento_copasst(request, id):
    data_nombramiento = archivos_copasst.objects.get(id=id)
    data_nombramiento.delete()
    
    return redirect('/nombramiento_copasst')

def listado_reunion_copasst(request):
    reuniones = reuniones_copasst.objects.all()

    return render(request, 'sst/copasst/listado_reunion_COPASST.html', {'lista_reuniones': reuniones})

def formulario_reunion_copasst(request, id):
    reuniones = reuniones_copasst.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_reuniones = reuniones_copasst.objects.get(id=id)
        variables_plantilla = {'id':id, 'acta':data_reuniones.acta, 'fecha':data_reuniones.fecha, 'lista_reuniones':reuniones , 'action_text':"Actualizar acta"}

    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0, 'acta':'', 'fecha':'', 'lista_reuniones':reuniones , 'action_text':"Agregar acta"}

    return render(request, 'sst/copasst/formulario_reunion_COPASST.html', variables_plantilla)
    
def agregar_reunion_copasst(request):
    if request.POST['id'] == '0':
        print("Nueva")

        if request.FILES['acta']:
            acta_file = request.FILES['acta']
            fs = FileSystemStorage()
            filename = fs.save(acta_file.name, acta_file)
            uploaded_file_url_acta = fs.url(filename)
                        
        print(request.POST)
        nueva_reunion = reuniones_copasst(fecha=request.POST['fecha'], acta=uploaded_file_url_acta)
        nueva_reunion.save()

    reunion = reuniones_copasst.objects.all()

    return redirect('/reunion_copasst')

def eliminar_reunion_copasst(request, id):
    data_reunion = reuniones_copasst.objects.get(id=id)
    data_reunion.delete()
    
    return redirect('/reunion_copasst')

#  COCOLA
def listado_cocola(request):
    miembros = cocola.objects.all()
    quejas = quejas_cocola.objects.all()
    
    return render(request, 'sst/cocola/listado_COCOLA.html', {'lista_miembros':miembros, 'lista_quejas':quejas})

def formulario_cocola(request, id):
    miembros = cocola.objects.all()
    if id !=0 : 
        print ("Actualizar registro")
        data_miembro = cocola.objects.get(id=id)
        variables_plantilla = {'id':id,'nombre':data_miembro.nombre, 'apellido':data_miembro.apellido, 'cedula':data_miembro.cedula, 'email':data_miembro.email, 'telefono':data_miembro.telefono, 'cargo':data_miembro.cargo, 'lista_miembros':miembros , 'action_text':"Actualizar miembro"}
    else:
        print ("Nuevo registro")
        variables_plantilla = {'id':0,'nombre':'', 'apellido':'', 'cedula':'', 'email':'', 'telefono':'', 'cargo':'', 'lista_miembros':miembros , 'action_text':"Agregar miembro"}

    return render(request, 'sst/cocola/formulario_COCOLA.html', variables_plantilla)

def agregar_cocola(request):
    if request.POST['id'] == '0':
        print("Nueva")
        nuevo_cocola = cocola(nombre=request.POST['nombre'], apellido=request.POST['apellido'], cedula=request.POST['cedula'], email=request.POST['email'], telefono=request.POST['telefono'], cargo=request.POST['cargo'])
        nuevo_cocola.save()

    else:
        print("Actualiza")
        data_cocola = cocola.objects.get(id=request.POST['id'])
        data_cocola.nombre = request.POST['nombre']
        data_cocola.apellido = request.POST['apellido']   
        data_cocola.cedula = request.POST['cedula']
        data_cocola.email = request.POST['email']
        data_cocola.telefono = request.POST['telefono']
        data_cocola.cargo = request.POST['cargo']
        data_cocola.save()

    miembros = cocola.objects.all()

    return redirect('/cocola')

def eliminar_cocola(request, id):
    data_cocola = cocola.objects.get(id=id)
    data_cocola.delete()
    return redirect('/cocola')

def listado_quejas_cocola(request):
    quejas = quejas_cocola.objects.all()

    return render(request, 'sst/cocola/listado_COCOLA.html', {'lista_quejas':quejas})

def formulario_quejas_cocola(request, id):
    quejas = quejas_cocola.objects.all()
    if id != 0:
        data_queja =quejas_cocola.objects.get(id=id)
        variables_plantilla = {'id':id,'miembro':data_queja.miembro, 'descripcion':data_queja.descripcion, 'fechaInscripcion':data_queja.fechaInscripcion, 'lista_quejas':quejas , 'action_text':"Actualizar queja"}
    else:
        variables_plantilla = {'id':0,'miembro':'', 'descripcion':'', 'fechaInscripcion':'', 'lista_quejas':quejas , 'action_text':"Agregar queja"}
    return render(request, 'sst/cocola/formulario_quejas_COCOLA.html', variables_plantilla)

def agregar_quejas_cocola(request):
    if request.POST['id'] == '0':
        nuevo_queja = quejas_cocola(miembro=request.POST['miembro'], descripcion=request.POST['descripcion'], fechaInscripcion=request.POST['fechaInscripcion'])
        nuevo_queja.save()

    else:
        print("Actualiza")
        data_queja = quejas_cocola.objects.get(id=request.POST['id'])
        data_queja.miembro = request.POST['miembro']
        data_queja.descripcion = request.POST['descripcion']   
        data_queja.fechaInscripcion = request.POST['fechaInscripcion']
        data_queja.save()

    quejas = quejas_cocola.objects.all()

    return redirect('/cocola')

#COMPROMISOS Y RESPONSABILIDADES

def formulario_compromisos(request,id):
    if id !=0 : 
        compromisos = Compromisos.objects.get(id=id)
        fechaFormat = date.isoformat(compromisos.fecha)
        variables_plantilla = {'id':id,'empresa':compromisos.empresa, 'nit':compromisos.nit, 'compromisos':compromisos.compromisos, 'firma':compromisos.firma, 'fecha':fechaFormat, 'firma_img':compromisos.firma_img}
    else:
        variables_plantilla = {'id':0,'empresa':'', 'nit':'', 'compromisos':'', 'firma':'', 'fecha':'','firma_img':''}

    return render(request, 'sst/formulario_compromisos.html', variables_plantilla)

def agregar_compromisos(request):
    if request.POST['id'] == '0':

        if request.FILES['firma_img']:
            firma_file = request.FILES['firma_img']
            fs = FileSystemStorage()
            filename = fs.save(firma_file.name, firma_file)
            uploaded_file_url_firma= fs.url(filename)

        nuevo_compromiso = Compromisos(empresa=request.POST['empresa'], nit=request.POST['nit'], compromisos=request.POST['compromisos'],firma=request.POST['firma'], fecha=request.POST['fecha'],firma_img = uploaded_file_url_firma)
        nuevo_compromiso.save()

    else:
        compromisos = Compromisos.objects.get(id=request.POST['id'])

        firma_file = request.FILES['firma_img']
        fs = FileSystemStorage()
        filename = fs.save(firma_file.name, firma_file)
        uploaded_file_url_firma= fs.url(filename)

        compromisos.empresa = request.POST['empresa']
        compromisos.nit = request.POST['nit']   
        compromisos.compromisos = request.POST['compromisos']
        compromisos.firma = request.POST['firma']
        compromisos.fecha = request.POST['fecha']
        compromisos.uploaded_file_url_firma = request.FILES['firma_img']
        compromisos.save()

    plts = Compromisos.objects.all()
    return render(request, 'sst/compromisos.html', {'compromisos': plts})

def eliminar_compromisos(request, id):
    compromiso = Compromisos.objects.filter(id=id).delete()
    plts = Compromisos.objects.all()
    # return render(request, 'sst/compromisos.html', {'compromisos': plts})
    return redirect('/b_compromisos')

def ver_compromisos(request):
    plts = Compromisos.objects.all()
    plts2 = Responsabilidades.objects.all()
    return render(request, 'sst/compromisos.html', {'compromisos': plts,'responsabilidades': plts2})

def pdf_compromisos(request, id,*args, **kwargs):
    plts = Compromisos.objects.get(id=id)
    data = {
            'empresa': plts.empresa,
            'nit': plts.nit,
            'compromisos': plts.compromisos,            
            'firma': plts.firma,
            'fecha': plts.fecha,
            'firma_img':plts.firma_img
        }
    pdf = render_to_pdf('sst/pdf_compromisos.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

### RESPONSABILIDADES

def formulario_responsabilidades(request,id):
    if id !=0 : 
        responsabilidades = Responsabilidades.objects.get(id=id)
        fechaFormat = date.isoformat(responsabilidades.fecha)
        variables_plantilla = {'id':id,'empresa':responsabilidades.empresa, 'nit':responsabilidades.nit, 'responsabilidades':responsabilidades.responsabilidades, 'firma':responsabilidades.firma, 'fecha':fechaFormat, 'firma_img':responsabilidades.firma_img}
    else:
        variables_plantilla = {'id':0,'empresa':'', 'nit':'', 'responsabilidades':'', 'firma':'', 'fecha':'','firma_img':''}

    return render(request, 'sst/formulario_responsabilidades.html', variables_plantilla)

def agregar_responsabilidades(request):
    if request.POST['id'] == '0':

        if request.FILES['firma_img']:
            firma_file = request.FILES['firma_img']
            fs = FileSystemStorage()
            filename = fs.save(firma_file.name, firma_file)
            uploaded_file_url_firma= fs.url(filename)

        nueva_responsabilidad = Responsabilidades(empresa=request.POST['empresa'], nit=request.POST['nit'], responsabilidades=request.POST['responsabilidades'],firma=request.POST['firma'], fecha=request.POST['fecha'],firma_img = uploaded_file_url_firma)
        nueva_responsabilidad.save()

    else:
        data_responsabilidades = Responsabilidades.objects.get(id = request.POST['id'])

        firma_file = request.FILES['firma_img']
        fs = FileSystemStorage()
        filename = fs.save(firma_file.name, firma_file)
        uploaded_file_url_firma = fs.url(filename)

        # data_responsabilidades = Responsabilidades.objects.get(id=request.POST['id'])
        data_responsabilidades.empresa = request.POST['empresa']
        data_responsabilidades.nit = request.POST['nit']   
        data_responsabilidades.responsabilidades = request.POST['responsabilidades']
        data_responsabilidades.firma = request.POST['firma']
        data_responsabilidades.fecha = request.POST['fecha']
        data_responsabilidades.uploaded_file_url_firma = request.FILES['firma_img']
        data_responsabilidades.save()

    plts = Responsabilidades.objects.all()
    # return render(request, 'sst/responsabilidades.html', {'responsabilidades': plts})
    return redirect('/b_compromisos')

def eliminar_responsabilidades(request, id):
    data_responsabilidades = Responsabilidades.objects.filter(id=id).delete()
    plts = Responsabilidades.objects.all()
    # return render(request, 'sst/responsabilidades.html', {'responsabilidades': plts})
    return redirect('/b_compromisos')

def ver_responsabilidades(request):
    plts = Responsabilidades.objects.all()
    return render(request, 'sst/responsabilidades.html', {'responsabilidades': plts})

def pdf_responsabilidades(request, id,*args, **kwargs):
    plts = Responsabilidades.objects.get(id=id)
    print(os.system('dir'))
    data = {
            'empresa': plts.empresa,
            'nit': plts.nit,
            'responsabilidades': plts.responsabilidades,            
            'firma': plts.firma,
            'fecha': plts.fecha,
            'firma_img':plts.firma_img
        }
    pdf = render_to_pdf('sst/pdf_responsabilidades.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

