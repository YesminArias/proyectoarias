from django import forms

class ingresar_Form(forms.Form):
    
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    edad= forms.IntegerField()