from django.shortcuts import render
from miApp.models import Familia 
from miApp.models import Amigos
from miApp.models import Compañeros
# Create your views here.
def mostrar_familia(request):
   f1 = Familia(nombre='juan', apellido='molina', email='juan@gmail.com')
   f2 = Familia(nombre='maria', apellido='arias', email='maria@gmail.com')
   f3 = Familia(nombre='Sonia', apellido= 'Esparza', email='socorro@gmail.com')
   f4 = Familia(nombre='Antonio', apellido= 'Arias Perez', email='antonio@gmail.com')
   f5 = Familia(nombre='Briany Valeria', apellido= 'Molina Arias', email='briany@gmail.com')
   f6 = Familia(nombre='Jhon Edison', apellido= 'Arias Esparza', email='jhon@gmail.com')
    
   return render(request, 'familia.html', {'familia':[f1, f2, f3, f4, f5, f6]})

def mostrar_amigos(request):
   a1 = Amigos(nombre='juan', apellido='molina', email='juan@gmail.com')
   a2 = Amigos(nombre='maria', apellido='arias', email='maria@gmail.com')
   a3 = Amigos(nombre='Sonia', apellido= 'Esparza', email='socorro@gmail.com')
   a4 = Amigos(nombre='Antonio', apellido= 'Arias Perez', email='antonio@gmail.com')
   a5 = Amigos(nombre='Briany Valeria', apellido= 'Molina Arias', email='briany@gmail.com')
   a6 = Amigos(nombre='Jhon Edison', apellido= 'Arias Esparza', email='jhon@gmail.com')
    
   return render(request, 'amigos.html', {'amigos':[a1, a2, a3, a4, a5, a6]})

def mostrar_compañeros(request):
   c1 = Compañeros(nombre='juan', apellido='molina', email='juan@gmail.com')
   c2 = Compañeros(nombre='maria', apellido='arias', email='maria@gmail.com')
   c3 = Compañeros(nombre='Sonia', apellido= 'Esparza', email='socorro@gmail.com')
   c4 = Compañeros(nombre='Antonio', apellido= 'Arias Perez', email='antonio@gmail.com')
   c5 = Compañeros(nombre='Briany Valeria', apellido= 'Molina Arias', email='briany@gmail.com')
   c6 = Compañeros(nombre='Jhon Edison', apellido= 'Arias Esparza', email='jhon@gmail.com')
    
   return render(request, 'compañeros.html', {'compañeros':[c1, c2, c3, c4, c5, c6]})

def mostrar_inicio(request):
  
    
   return render(request, 'index.html')