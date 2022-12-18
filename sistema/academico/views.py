from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Curso
# Create your views here.


def home(request):
    
    curso = Curso.objects.all()
    return render(request, 'home.html',{
        'curso':curso
    })

def registrarte(request):
    if request.method == 'GET':
        return render(request, './authenticated/registrarse.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
            
            
        else:
            return render(request, './authenticated/registrarse.html',{
                'form':UserCreationForm,
                'error':'Las contrasenias no coinsiden'
            })

def iniciar_sesion(request):
    if request.method =='GET':
        return render(request,'./authenticated/iniciar_sesion.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password =request.POST['password'])
        if user is None:
            return render(request,'./authenticated/iniciar_sesion.html',{
            'form':AuthenticationForm,
            'error':'No se encontro la cuenta'
        })
        else:
            login(request, user)
            return redirect('home')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')




def registrar_curso(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numcredito']
    
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos = creditos)
    return redirect('home')

def editar_curso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'editar_curso.html',{
        'curso':curso
    })
    
def edicion_curso(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numcredito']
    curso = Curso.objects.get(codigo=codigo)
    
    curso.nombre = nombre 
    curso.creditos = creditos
    curso.save()
    return redirect('home')

def eliminar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('home')
    