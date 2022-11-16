from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    edad = models.IntegerField(max_length=4)

class Amigos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    edad = models.IntegerField(max_length=4)
    
class Compañeros(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    edad = models.IntegerField(max_length=4)