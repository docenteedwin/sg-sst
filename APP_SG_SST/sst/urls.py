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

    path('encargado', views.formulario_encargado, name='encargado'),
    path('configuracion_empresa', views.formulario_configuracion, name='configuracion_empresa'),
    path('compromisos', views.formulario_compromisos, name='configuracion_empresa'),
    path('aliados', views.listado_aliados, name='aliados'),
    path('formulario_aliados', views.formulario_aliados, name='formulario_aliados'),
    path('riesgos', views.formulario_riesgos, name='riesgos'),
    path('plan_emergencia', views.formulario_plan_emergencia, name='plan_emergencia'),

    # USUARIOS

    path('usuarios', views.listado_usuarios, name='usuarios'),
    path('formulario_usuarios/<int:id>', views.formulario_usuarios, name='formulario_usuarios'),
    path('agregar_usuarios', views.agregar_usuarios, name='agregar_usuarios'),

    #POLITICAS

    path('formulario_politicas/<int:id>', views.formulario_politicas, name='formulario_politicas'),
    path('agregar_politicas', views.agregar_politicas, name='agregar_politicas'),
    path('politicas', views.ver_politicas, name='politicas'),
    path('eliminar_politicas/<int:id>', views.eliminar_politicas, name='eliminar_politicas'),

]