
from operator import truediv
from pyexpat import model
from django.db import models

# Create your models here.
class Clientes(models.Model):
    Cuit=models.CharField(max_length=10)
    RSocial=models.CharField(max_length=40)
    Domicilio=models.CharField(max_length=40)
    Mail=models.EmailField()
    Telefono=models.CharField(max_length=10)
    Activo=models.BooleanField()
    
class Articulos(models.Model):
    Codigo=models.CharField(max_length=10)
    Descripcion=models.CharField(max_length=40)
    UnidadMedida=models.CharField(max_length=3)
    Precio=models.IntegerField()
    
class Pedidos(models.Model):
    NroPedido=models.IntegerField()
    Fecha=models.DateField()
    CuitCliente=models.CharField(max_length=10)
    Importe=models.DecimalField(decimal_places=2, max_digits=10)
    
class PedidoDetalle(models.Model):
    NroPedido=models.IntegerField()
    Articulo=models.CharField(max_length=10)
    Cantidad=models.IntegerField()
    Punitario=models.DecimalField(decimal_places=2, max_digits=10)
    