from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Grupo(models.Model):
    owner = models.ForeignKey(User)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    owner = models.ForeignKey(User)
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, verbose_name='tel')
    grupo = models.ForeignKey(Grupo)

    def __str__(self):
        return self.nombre
