from multiprocessing.sharedctypes import Value
from wsgiref.util import request_uri
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from AppPedidos.models import Articulos, Clientes, Pedidos
from django.template import loader
from AppPedidos.forms import AbmCliente_formulario, AbmArticulo_formulario, AbmPedido_formulario



# Create your views here.

def inicio(request):
    return render(request,"menu.html")

def leer_clientes(request):
    clientes = Clientes.objects.all()
    texto = "leerclientes"
    return  HttpResponse( clientes )



def abm_clientes(request):
    return render(request, "abmclientes.html")



def alta_clientes(request):
    if request.method == 'POST':
        mi_formulario = AbmCliente_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            #return  HttpResponse ( datos )
            ##cliente = Clientes(Cuit = request.POST['Cuit'], RSocial=request.POST['RSocial'], Domicilio=request.POST['Domi'], Mail=request.POST['Mail'], Telefono=request.POST['Tele'] ,Activo=xactivo )
            cliente = Clientes( Cuit = datos['cuit'], RSocial=datos['rsocial'], Domicilio=datos['domicilio'],Mail=datos['mail'],Telefono=datos['telefono'], Activo = datos['activo'] )
            cliente.save()
            textoresultado ="El registro fue grabado OK!!"  
            return  HttpResponse(textoresultado)
        else:
            textodeerror ="Is Valid false"  
            return  HttpResponse(textodeerror)
            #return render(request, "abmclientes.html")
    return render(request="abmclientes.html")   
        

def abm_articulos(request):
    return render(request, "abmArticulo.html")

def alta_articulos(request):
    if request.method == 'POST':
        mi_formulario = AbmArticulo_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            articulo = Articulos( Codigo = datos['codigo'], Descripcion=datos['descrip'], UnidadMedida=datos['um'],Precio=datos['puni'] )
            articulo.save()
            textoresultado ="El registro fue grabado OK!!"  
            return  HttpResponse(textoresultado)
        else:
            textodeerror ="Is Valid false"  
            return  HttpResponse(textodeerror)
            #return render(request, "abmclientes.html")
    return render(request="abmArticulo.html")


def abm_pedidos(request):
    return render(request, "abmpedidos.html")


def alta_pedido(request):
    if request.method == 'POST':
        mi_formulario = AbmPedido_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            #print (datos)
            pedido =  Pedidos( NroPedido = datos['nropedido'], Fecha=datos['fecha'], CuitCliente=datos['cuit'],Importe=datos['importe'] )
            pedido.save()
            textoresultado ="El registro de pedidofue grabado OK!!"  
            return  HttpResponse(textoresultado)
        else:
            textodeerror ="Is Valid false"  
            return  HttpResponse(textodeerror)
            #return render(request, "abmclientes.html")
    return render(request="abmArticulo.html")



def buscar_articulos(request):
   # if request.GET['descripcion']:
   #     descripbusqueda = request.GET['descripcion']
   #     resultado = Articulos.objects.filter(Descripcion_icontains = descripbusqueda)
   #     return render (request, "resultado_buscararticulo.html", {"resultado" : descripbusqueda})
   # else:
   #     return HttpResponse ("campo vacio")
   # return HttpResponse (f"estamos buscando articulos con {request.GET['descripcion']}")
    #return render(request,  "buscar_articulo.html")
    return render(request, "buscar_articulo.html")

def buscar(request):
    
    if request.GET['nombre']:
        nombre =request.GET['nombre']
        cursos = Articulos.objects.filter(Descripcion__icontains = nombre)
        print (cursos)
        return render( request, "resultado_buscararticulo.html" , {"cursos", cursos})
        #return HttpResponse (f"Estamos buscadno { request.GET['nombre']}")
    else:
        return HttpResponse ("campo de busqueda vacio")