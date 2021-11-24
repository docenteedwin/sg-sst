from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('acceder', views.acceder, name='acceder'),

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

    #COCOLA
    path('cocola', views.listado_cocola, name='cocola'),
    path('formulario_cocola/<int:id>', views.formulario_cocola, name='formulario_cocola'),
    path('agregar_cocola', views.agregar_cocola, name='agregar_cocola'),
    path('eliminar_cocola/<int:id>', views.eliminar_cocola, name='eliminar_cocola'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)