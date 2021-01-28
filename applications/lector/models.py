from django.db import models

# Create your models here.
from .managers import PrestamoManager
from applications.libro.models import Libro


class Lector(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=20)
    edad = models.PositiveIntegerField('Edad', default=0)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
    

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE, verbose_name='Lector')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name='Libro', related_name='libro_prestamo')
    fecha_prestamo = models.DateField('Fecha del prestamo')
    fecha_devolucion = models.DateField('Fecha de la devolución', blank=True, null=True)
    devuelto = models.BooleanField('Regresado', default=False)

    objects = PrestamoManager()

    def __str__(self):
        return str(self.id) + '-prestamo ' + self.libro.titulo


    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'