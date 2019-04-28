# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DatosPersonales(models.Model):
    Num_count=models.CharField(max_length=100, primary_key=True)
    Nombre=models.CharField(max_length=20)
    Sexo=models.CharField(max_length=1)
    Edad=models.IntegerField()
    FechaNacimiento=models.DateField()
    Telefono=models.CharField(max_length=10)
    Email=models.EmailField()
    Domicilio=models.TextField()

# Create your models here.
