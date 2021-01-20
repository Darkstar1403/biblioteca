from django.db import models

# Create your models here.
from .managers import AutorManager

class Autor(models.Model):
    nombre = models.CharField('Nombres', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=30)
    edad = models.PositiveIntegerField('Edad')

    objects = AutorManager()

    def __str__(self):
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'