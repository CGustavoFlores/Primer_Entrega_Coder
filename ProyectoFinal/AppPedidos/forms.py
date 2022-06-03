from django import forms

class AbmCliente_formulario(forms.Form):
    
    cuit= forms.CharField(max_length=10)
    rsocial= forms.CharField(max_length=40)
    domicilio= forms.CharField(max_length=40)
    mail=forms.EmailField()
    telefono=forms.CharField( max_length=10)
    activo=forms.CharField(max_length=2)




class AbmArticulo_formulario(forms.Form):

    codigo=forms.CharField(max_length=10)
    descrip=forms.CharField(max_length=40)
    um=forms.CharField(max_length=3) 
    puni=forms.IntegerField()
    
    
    
    
class AbmPedido_formulario(forms.Form):
    
    nropedido = forms.IntegerField()
    fecha= forms.DateField()
    cuit=forms.CharField(max_length=10)
    importe=forms.DecimalField(decimal_places=2,max_digits=10)
    
    
    