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
            data_producto = producto_aliado.objects.get(id=id)
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

# Comites

# COCOLA
def listado_cocola(request):
    pass

def agregar_miembro_cocla(request):
    pass

