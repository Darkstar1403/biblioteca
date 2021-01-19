from django.db import models

# Create your models here.
from applications.libro.models import Libro


class Lector(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=20)
    edad = models.PositiveIntegerField('Edad', default=0)
    
    def __str__(self):
        return self.nombre
    

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE, verbose_name='Lector')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name='Libro')
    fecha_prestamo = models.DateField('Fecha del prestamo')
    fecha_devolucion = models.DateField('Fecha de la devolución', blank=True, null=True)
    devuelto = models.BooleanField('Regresado', default=False)

    def __str__(self):
        return self.id + '-prestamo ' + self.libro.titulo