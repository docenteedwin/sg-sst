from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('acceder', views.acceder, name='acceder'),
    path('logout', views.logout, name='logout'),

    # DOCUMENTACION

    # Empresa 
    path('lista_empresa', views.listado_empresa, name='lista_empresa'),
    path('formulario_empresa/<int:id>', views.formulario_empresa, name='formulario_empresa'),
    path('agregar_empresa', views.agregar_empresa, name='agregar_empresa'),
    path('eliminar_empresa/<int:id>', views.eliminar_empresa, name='eliminar_empresa'),
    
    # Encargado
    
    path('encargado', views.listado_encargado, name='encargado'),
    path('formulario_encargado/<int:id>', views.formulario_encargado, name='formulario_encargado'),
    path('agregar_encargado', views.agregar_encargado, name='agregar_encargado'), 
      
    path('compromisos', views.formulario_compromisos, name='configuracion_empresa'),

    # Riesgo psicosocial y plan de emergencia
    path('riesgos', views.listado_riesgos, name='riesgos'),
    path('formulario_riesgos/<int:id>', views.formulario_riesgos, name='formulario_riesgos'),
    path('agregar_riesgos', views.agregar_riesgos, name='agregar_riesgos'),

    # ALIADOS

    path('aliados', views.listado_aliados, name='aliados'),
    path('formulario_aliados/<int:id>', views.formulario_aliados, name='formulario_aliados'),
    path('agregar_aliados', views.agregar_aliados, name='agregar_aliados'),
    path('eliminar_aliados/<int:id>', views.eliminar_aliados, name='eliminar_aliados'),
    
    path('formulario_productos/<int:id>/<int:aliado>', views.formulario_productos ,name='formulario_productos'),
    path('agregar_productos', views.agregar_productos, name='agregar_productos'),
    path('eliminar_productos/<int:id>', views.eliminar_productos, name='eliminar_productos'),
    
    # USUARIOS

    path('usuarios', views.listado_usuarios, name='usuarios'),
    path('formulario_usuarios/<int:id>', views.formulario_usuarios, name='formulario_usuarios'),
    path('agregar_usuarios', views.agregar_usuarios, name='agregar_usuarios'),
    path('eliminar_usuarios/<int:id>', views.eliminar_usuarios, name='eliminar_usuarios'),

    #POLITICAS

    path('politicas', views.ver_politicas, name='politicas'),
    path('formulario_politicas/<int:id>', views.formulario_politicas, name='formulario_politicas'),
    path('agregar_politicas', views.agregar_politicas, name='agregar_politicas'),
    path('eliminar_politicas/<int:id>', views.eliminar_politicas, name='eliminar_politicas'),
    path('pdf_politicas/<int:id>', views.pdf_politicas, name='pdf_politicas'),

    # COMPROMISOS

    path('b_compromisos', views.ver_compromisos, name='compromisos'),
    path('formulario_compromisos/<int:id>', views.formulario_compromisos, name='formulario_compromisos'),
    path('agregar_compromisos', views.agregar_compromisos, name='agregar_compromisos'),
    path('eliminar_compromisos/<int:id>', views.eliminar_compromisos, name='eliminar_compromisos'),
    path('pdf_compromisos/<int:id>', views.pdf_compromisos, name='pdf_compromisos'),
    
    # RESPONSABILIDADES

    path('b_responsabilidades', views.ver_responsabilidades, name='responsabilidades'),
    path('formulario_responsabilidades/<int:id>', views.formulario_responsabilidades, name='formulario_responsabilidades'),
    path('agregar_responsabilidades', views.agregar_responsabilidades, name='agregar_responsabilidades'),
    path('eliminar_responsabilidades/<int:id>', views.eliminar_responsabilidades, name='eliminar_responsabilidades'),
    path('pdf_responsabilidades/<int:id>', views.pdf_responsabilidades, name='pdf_responsabilidades'),
    
    # MODULO COMITES
    
    # COPASST
    path('copasst', views.listado_copasst, name='copasst'),
    path('formulario_copasst/<int:id>', views.formulario_copasst, name='formulario_copasst'),
    path('agregar_copasst', views.agregar_copasst, name='agregar_copasst'),
    path('eliminar_copasst/<int:id>', views.eliminar_copasst, name='eliminar_copasst'),
    path('plan_copasst', views.listado_plan_copasst, name='plan_copasst'),
    path('formulario_plan_copasst/<int:id>', views.formulario_plan_copasst, name='formulario_plan_copasst'),
    path('agregar_plan_copasst', views.agregar_plan_copasst, name='agregar_plan_copasst'),
    path('eliminar_plan_copasst/<int:id>', views.eliminar_plan_copasst, name='eliminar_plan_copasst'),
    path('votacion_copasst', views.listado_votacion_copasst, name='votacion_copasst'),
    path('formulario_votacion_copasst/<int:id>', views.formulario_votacion_copasst, name='formulario_votacion_copasst'),
    path('agregar_votacion_copasst', views.agregar_votacion_copasst, name='agregar_votacion_copasst'),
    path('eliminar_votacion_copasst/<int:id>', views.eliminar_votacion_copasst, name='eliminar_votacion_copasst'),
    path('nombramiento_copasst', views.listado_nombramiento_copasst, name='nombramiento_copasst'),
    path('formulario_nombramiento_copasst/<int:id>', views.formulario_nombramiento_copasst, name='formulario_nombramiento_copasst'),
    path('agregar_nombramiento_copasst', views.agregar_nombramiento_copasst, name='agregar_nombramiento_copasst'),
    path('eliminar_nombramiento_copasst/<int:id>', views.eliminar_nombramiento_copasst, name='eliminar_nombramiento_copasst'),
    path('reunion_copasst', views.listado_reunion_copasst, name='reunion_copasst'),
    path('formulario_reunion_copasst/<int:id>', views.formulario_reunion_copasst, name='formulario_reunion_copasst'),
    path('agregar_reunion_copasst', views.agregar_reunion_copasst, name='agregar_reunion_copasst'),
    path('eliminar_reunion_copasst/<int:id>', views.eliminar_reunion_copasst, name='eliminar_reunion_copasst'),

    #COCOLA
    path('cocola', views.listado_cocola, name='cocola'),
    path('formulario_cocola/<int:id>', views.formulario_cocola, name='formulario_cocola'),
    path('agregar_cocola', views.agregar_cocola, name='agregar_cocola'),
    path('eliminar_cocola/<int:id>', views.eliminar_cocola, name='eliminar_cocola'),
    path('formulario_queja_cocola/<int:id>', views.formulario_quejas_cocola, name='formulario_queja_cocola'),
    path('agregar_queja', views.agregar_quejas_cocola, name='agregar_queja'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)