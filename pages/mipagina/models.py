from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.

#modelo del usario personalizado del proyecto final
class UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    genero = models.CharField(null=True,blank=True, max_length=1)
    

#se presntan los diferentes modelos de la base de datos diseñada en posgres 
#modelo de las ciudades 
class Ciudad(models.Model):
    nombre = models.TextField(default="")
    
    def __str__(self):
        return self.nombre

#modelo de hospedaje en la base de datos 
class Hospedaje(models.Model):
    ciudad = models.TextField(default="")
    beneficios = models.TextField(default="")
    presio = models.TextField(default="")
    img = models.TextField(default="")
    
    def __str__(self):
        return self.ciudad

#modelo de vuelo en la base de datos 
class Vuelo(models.Model):
    ciudad = models.TextField(default="")
    descrpicion = models.TextField(default="")
    escala = models.TextField(default="")
    presio = models.TextField(default="")
    img = models.TextField(default="")
    
    def __str__(self):
        return self.ciudad

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])

#modelo de viaje en la base de datos 
class Viaje(models.Model):
    ciudad = models.TextField(default="")
    descrpicion = models.TextField(default="")
    presio = models.TextField(default="")
    img = models.TextField(default="")
    noches = models.TextField(default="")

    def __str__(self):
        return self.ciudad

    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])

