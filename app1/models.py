from django.db import models

# Create your models here.

class Vuelo(models.Model):
    id_vuelo = models.IntegerField()
    salida = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    fecha = models.DateField()    #2022-05-23(AAAA-MM-DD)
    hora_de_salida = models.TimeField() #02:13(HH:MM)

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    id_vuelo = models.IntegerField()

class Pasajero(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    id_vuelo = models.IntegerField()