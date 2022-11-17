from django.shortcuts import render
from miApp.models import Familia 
from miApp.models import Amigos
from miApp.models import Compañeros
from .forms import ingresar_Form
# Create your views here.
def mostrar_familia(request):
   f1 = Familia(nombre='juan', apellido='molina', email='juan@gmail.com',edad='40')
   f2 = Familia(nombre='maria', apellido='arias', email='maria@gmail.com',edad='50')
   f3 = Familia(nombre='Sonia', apellido= 'Esparza', email='socorro@gmail.com',edad='60')
   f4 = Familia(nombre='Antonio', apellido= 'Arias Perez', email='antonio@gmail.com',edad='80')
   f5 = Familia(nombre='Briany Valeria', apellido= 'Molina Arias', email='briany@gmail.com',edad='6')
   f6 = Familia(nombre='Jhon Edison', apellido= 'Arias Esparza', email='jhon@gmail.com',edad='35')
    
   return render(request, 'familia.html', {'familia':[f1, f2, f3, f4, f5, f6]})

def mostrar_amigos(request):
   a1 = Amigos(nombre='Mario', apellido='Rincon', email='mario@gmail.com',edad='40')
   a2 = Amigos(nombre='Tatiana', apellido='Ramon', email='Tatiana@gmail.com',edad='20')
   a3 = Amigos(nombre='Sergio', apellido= 'Bermudez', email='sergio@gmail.com',edad='33')
   a4 = Amigos(nombre='Alexander', apellido= 'Peña', email='Alexander@gmail.com',edad='30')
   a5 = Amigos(nombre='Maye', apellido= 'Garcia', email='maye@gmail.com',edad='30')
   a6 = Amigos(nombre='Anyel', apellido= 'Ovalles', email='anyel@gmail.com',edad='20')
    
   return render(request, 'amigos.html', {'amigos':[a1, a2, a3, a4, a5, a6]})

def mostrar_compañeros(request):
   c1 = Compañeros(nombre='Isabela', apellido='Rodriguez', email='Isabel@gmail.com',edad='30')
   c2 = Compañeros(nombre='Felipe', apellido='Molina', email='felipe@gmail.com',edad='20')
   c3 = Compañeros(nombre='Maykol', apellido= 'Espinal', email='maykol@gmail.com',edad='35')
   c4 = Compañeros(nombre='Gibran', apellido= 'Raydan', email='gibran@gmail.com',edad='39')
   c5 = Compañeros(nombre='Nicolas', apellido= 'Bermudez', email='nico@gmail.com',edad='25')
   c6 = Compañeros(nombre='Laura', apellido= 'Peña', email='laura@gmail.com',edad='43')
    
   return render(request, 'compañeros.html', {'compañeros':[c1, c2, c3, c4, c5, c6]})

def mostrar_inicio(request):
  
    
   return render(request, 'index.html')

def ingresar_amigo(request):
    
    if request.method == 'POST':
        
        formulario = ingresar_Form(request.POST)
        
        if formulario.is_valid():
            
            formulario_limpio = formulario.cleaned_data
        
            amigo = Amigos(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'],email=formulario_limpio['email'],edad=formulario_limpio['edad'])
       
            amigo.save()
        
            return render(request, 'index.html')
    else: 
        formulario = ingresar_Form()
    
    return render(request, 'ingresar_amigo.html', {'formulario': formulario})
 
 
def buscar_amigos(request):
   
    return render (request, 'buscar_amigos.html')