from collections import UserDict, UserList
from .forms import ProductoForm, Producto
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from thebrickApp.Carrito import Carrito
from .forms import FormularioLogin, FormularioRegistro
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login



#Registro
def mostrar_registro(request):
    if request.method == 'GET':
        contexto = {
            'formulario': FormularioRegistro()
        }
        return render(request,'registration/registro.html', contexto)
    if request.method == 'POST':
        datos_formulario = FormularioRegistro(data=request.POST)
        print(datos_formulario.data)
        es_valido = datos_formulario.is_valid()
        print(es_valido)
        if es_valido: # Preguntamos por el True
            datos_formulario.save()
            username = datos_formulario.cleaned_data['username']
            (request, f'gracias por registrarte { username }')
            return redirect('login')
        contexto = {
            'formulario': datos_formulario
        }
    return render(request,'registration/registro.html',contexto)

#Login

def mostrar_entrar(request):
    if request.method == 'GET':
        contexto = {
            'formulario':FormularioLogin(),
            'titulo':'Bienvenido',
            'formulario_original': AuthenticationForm()
        }
        return render(request, 'registration/login.html',contexto)
    elif request.method == 'POST':
        datos_usuario = AuthenticationForm(data=request.POST)
        print(datos_usuario.data)
        es_valido = datos_usuario.is_valid()
        print(datos_usuario.errors)
        if es_valido:
            username = datos_usuario.cleaned_data['username']
            password = datos_usuario.cleaned_data['password']
            print(username,password)
            usuario = authenticate(username=username,password=password)
            if usuario is not None:
                login(request,usuario)
                return redirect('index')
            else:
                # Mandar al lobby
                return redirect('index')
        contexto = {
            'titulo':'Bienvenido',
            'formulario_original': datos_usuario,
            'formulario':FormularioLogin()
        }


def index(request):
    return render(request,'index.html')

def lanzamiento(request):
    return render(request,'lanzamiento.html')

def hombre(request):
    return render(request,'hombre.html')

def mujer(request):
    producto = Producto.objects.all()

    data = {
        'producto': producto
    }
    return render(request,'mujer.html',data)

def oferta(request):
    return render(request,'oferta.html' )

def formulario(request):
    return render(request,'formulario.html')

#CRUD

@login_required
def agregar_stock(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
    return render(request,'producto/agregar.html',data)

@login_required
def listar(request):
    producto = Producto.objects.all()

    data = {
        'producto': producto
    }

    return render(request,'producto/listar.html',data)

@login_required
def modificar(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Satisfactoriamente")
            return redirect(to="listar")
        data["form"] = formulario

    return render(request,'producto/modificar.html',data)

@login_required
def eliminar(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request,"Eliminado Satisfactoriamente")
    return redirect(to="listar")

#CARRITO 

def carrito(request):
    return render(request,'carrito.html')

def agregar_producto(request,id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request,id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def total_carrito(request):
    carrito = Carrito(request)
    context = {
        "total_carrito": Carrito.total_carrito()
    }
    total = carrito.total_carrito()
    return redirect(request, "carrito.html", context)