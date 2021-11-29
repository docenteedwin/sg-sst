"# sg-sst"

Para poder ingresar a la aplicación debemos tener instalado los siguientes programas:
Python superior a 3.9.6
postgresql 13
instalar django version 3.2.6
instalar django con el comando (revisar que estemos dentro del environment virtual):
desactivar antivirus, windows defender, firewall o cualquier software si falla este proceso
esto instala django y sus dependencias  python -m pip install django
Instalar psycopg2   sudo apt install python3-dev libpq-dev
  y pip install psycopg

1 . Antes de poder ejecutar el proyecto completo debemos configurar la base de datos la            
    cual se encuentra en el repositorio antes mencionado, realizaremos la respectiva   
    configuración y proceso para poder correr la base de datos.
  1.1 descargar postgresql e instalarlo con la siguiente configuración user “ postgres”  
    password “python1A”
 1.2 crear una base de datos con el nombre de “sst”
 1.3 Importar la base de datos adjunta en el repositorio
 1.4 Se abre el proyecto en visual code 
 1.5 Abrimos una nueva terminal 
 1.6  Escribimos  cd Scripts
 1.7 Activate
 1.8  cd..
 1.9 cd APP_SG_SST
1.10 python manage.py migrate
1.11 python manage.py makemigrations

2.Para ingresar al localhost se debe realizar el siguiente proceso:
  2.1 Se abre el proyecto clonado o descargado del repositorio 
  2.2 Si el proyecto lo abre con visual code, debe crear una nueva terminal con los permisos  
        del cmd, se realiza el siguiente comando para poder ejecutar la aplicación.
  2.3 cd Scripts
  2.4 Activate
  2.5 cd..
  2.6 cd APP_SG_SST
  2.7 python manage.py runserver
  2.8 abre el siguiente link de ingreso  http://127.0.0.1:8000/ 

3.Ingresar con email y contraseña, para poder ver el panel donde podremos iniciar sesión a la aplicación.  

4. Nos ubicamos en la parte izquierda superior donde encontramos los módulos que nos permiten navegar por las diferentes opciones que tiene la aplicación la cual cuenta con los siguientes módulos y dentro de cada módulo su respectivo proceso:

Documentación:  
    Encargado del sg-sst
    Configuración de empresa
    Compromiso y responsabilidades
    Aliados estratégicos 
    Política del SG-SST 
    Riesgos psicosociales
Usuarios:
    Lista de usuarios
    Agregar usuarios
Comités: 
    Cocola
    Copasst
    Brigada de emergencia
Salir:
