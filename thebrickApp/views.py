from collections import UserDict, UserList
from .forms import CustomUserCreationForm, ProductoForm, Producto
from django.shortcuts import render,redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import admin
from django.contrib import messages
from thebrickApp.Carrito import Carrito

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,)
            return redirect(to="index")
        data["form"] = formulario
    return render(request,'registration/registro.html',data)

def login(request):
    return render(request,'registration/login.html')

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