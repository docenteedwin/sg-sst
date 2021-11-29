from django.db import models
from django.utils import timezone


# Create your models here.

class users(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_surname = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255)
    identity_number = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    admin_status = models.CharField(max_length=255)
    activity_status = models.CharField(max_length=255)
    id_rol = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user_name

class rol(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name

class permissions(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Permission"
        verbose_name_plural = "Permissions"

    def __str__(self):
        return self.name

class permissions_role(models.Model):
    id_permission = models.IntegerField()
    id_rol = models.IntegerField()

    class Meta:
        verbose_name = "Permission_role"
        verbose_name_plural = "Permissions_role"

    def __str__(self):
        return self.id_rol

#Política del SG-SST
#Created: jose Luis Hoyos
#Fecha: 29/oct/2021

class Politicas(models.Model):
    empresa = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    compromisos = models.TextField()
    requisitos_legales = models.TextField()
    objetivos = models.TextField()
    comentarios = models.TextField()
    firma = models.CharField(max_length=30)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Politica"
        verbose_name_plural = "Politicas"

    def __str__(self):
        return self.empresa
        
# Configuración de la empresa

class empresa(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    georreferencia = models.CharField(max_length=255)
    actividad_economica = models.CharField(max_length=255)
    nivel_riesgo = models.CharField(max_length=255)
    cant_trabajadores = models.CharField(max_length=255)
    naturaleza_juridica = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=255)
    email_contacto = models.CharField(max_length=255)
    tipo_empresa = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre_empresa

class aliado(models.Model):
    name = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    arl = models.CharField(max_length=255)
    pago_seguridad_social = models.CharField(max_length=255)
    seguridad_producto = models.CharField(max_length=255)
    cumplimiento_arl = models.CharField(max_length=255)


    class Meta:
        verbose_name = "Aliado"
        verbose_name_plural = "Aliados"

    def __str__(self):
        return self.name

class producto_aliado(models.Model):
    aliado = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    seguridad_producto = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return self.nombre

class documento(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "media/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

class riesgos_emergencia(models.Model):
    riesgosFile =models.CharField(max_length=255)
    emergenciaFile =models.CharField(max_length=255)

# MODULO COMITES

class copasst(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)

class plan_copasst(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    
class archivos_copasst(models.Model):
    votacion = models.CharField(max_length=255)
    nombramiento = models.CharField(max_length=255)
    tipo_archivo = models.IntegerField()
    fecha = models.DateField()

class reuniones_copasst(models.Model):
    acta = models.CharField(max_length=255)
    fecha = models.DateField()

class cocola(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)

class quejas_cocola(models.Model):
    miembro = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    fechaInscripcion = models.DateField(auto_now=True)
