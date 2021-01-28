from django.db import models
import datetime

from django.db.models import Q, Count


class LibroManager(models.Manager):
    """Managers para el modelo autor"""

    def listarLibros(self):
       return self.all()

    def buscarLibro(self, valor):
        if(valor == None):
            resultado = self.all()[:10]
        else:
            resultado = self.filter(
                titulo__icontains=valor
            )
        return resultado

    def buscarLibroFecha(self, valor, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains=valor,
            fecha__range=(date1, date2)
        )
        return resultado

    def listarLibrosCategoria(self, categoria):

        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')

    def addAutorLibro(self, libroId, autor):
        libro = self.get(id=libroId)
        libro.autor.add(autor)
        return libro

    def delAutorLibro(self, libroId, autor):
        libro = self.get(id=libroId)
        libro.autor.remove(autor)
        return libro

    def librosNumPrestamos(self):
        #devuelve un diccionario de python aggregate
        resultado = self.aggregate(
            cantPrestamos = Count('libro_prestamo')
        )
        return resultado

    def numLibrosPrestados(self):
        #annotate se guia en base del pk del modelo por lo que gfue más facil
        #realizar el conteo de copias prestadas de un libro desde este modelo
        #usando el related_name
        resultado = self.annotate(
            numPrestados = Count('libro_prestamo')
        )
        for r in resultado:
            print(r, r.numPrestados)
        return resultado

class CategoriaManager(models.Manager):


    def categoriaPorAutor(self, autor):
        return self.filter(
            #usamos el related name para llegar de categoria a la tabla libro
            #luego __ oara ir al atributo autor y de ahi nos traemos
            #el id pero usando de nuevo __ ya que seria el de la tabla autor
            categoria_libro__autor__id = autor
        ).distinct()#evita que traiga consultas repetidas ya que si tenia 3 libros
    #en una misma categoria nos iba a repetir esa relacion 3 veces

    def listarCategoriaLibros(self):
        #es parecido a un groupBy de sql y agrega una columna al queryset 
        resultado = self.annotate(
            cantidadLibros=Count('categoria_libro')
        )
        for r in resultado:
            print(r, r.cantidadLibros)
        return resultado
