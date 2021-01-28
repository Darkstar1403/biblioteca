from django.db import models

# Create your models here.
from applications.autor.models import Autor
from applications.libro.managers import LibroManager, CategoriaManager


class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=30)

    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + '-' + self.nombre
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría', related_name='categoria_libro')
    autor = models.ManyToManyField(Autor,verbose_name='Autores')
    titulo = models.CharField('Titulo', max_length=50)
    fecha = models.DateField('Fecha de lanzamiento', auto_now=False, auto_now_add=False)
    portada = models.ImageField('Portada', upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField('No. de visitas')

    objects = LibroManager()
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha']


