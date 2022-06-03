from django.urls import path
from AppPedidos.models import Clientes , Articulos, Pedidos 
from . import views

urlpatterns = [
    
    path("", views.inicio),
    path("listarclientes", views.leer_clientes),
    path("clientes", views.abm_clientes, name="clientes"),
    path("alta_clientes",views.alta_clientes),
    path("articulos", views.abm_articulos, name = "articulos"),
    path("alta_articulos", views.alta_articulos), 
    path("pedidos", views.abm_pedidos, name="pedidos"),
    path("alta_pedido", views.alta_pedido),
    path("buscararticulo", views.buscar_articulos, name="buscararticulo"),
    path("buscar", views.buscar)
             
             ]