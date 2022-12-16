from django.shortcuts import render,redirect
from .models import Curso
# Create your views here.


def home(request):
    
    curso = Curso.objects.all()
    return render(request, 'home.html',{
        'curso':curso
    })
    
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
    