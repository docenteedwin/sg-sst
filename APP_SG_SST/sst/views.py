from django.shortcuts import render, redirect

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