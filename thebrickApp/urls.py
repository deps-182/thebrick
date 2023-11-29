from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('lanzamientos/',views.lanzamiento, name='lanzamiento'),
    path('hombre/',views.hombre, name='hombre'),
    path('mujer/',views.mujer, name='mujer'),
    path('oferta/',views.oferta, name='oferta'),
    path('formulario/',views.formulario,name='formulario'),
    path('registro/',views.mostrar_registro,name='mostrar_registro'), #Registro
    path('login/',views.mostrar_entrar, name = 'mostrar_entrar'), #Login
    path('accounts/',include('django.contrib.auth.urls')),
    path('agregar_stock/',views.agregar_stock, name="agregar_stock"),
    path('listar/',views.listar,name="listar"),
    path('modificar/<id>/',views.modificar,name="modificar"),
    path('eliminar/<id>/',views.eliminar, name = "eliminar"),
    path('carrito/',views.carrito,name="carrito"),
    path('agregar/<id>/', views.agregar_producto, name="Add"),#Carrito
    path('eliminar/<id>/', views.eliminar_producto, name="Del"),
    path('restar/<id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('total_carrito',views.total_carrito,name="total_carrito"),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)