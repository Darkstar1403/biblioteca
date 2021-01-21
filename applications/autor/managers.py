from django.db import models

from django.db.models import Q


class AutorManager(models.Manager):
    """Managers para el modelo autor"""

    def listarAutores(self):
       return self.all()

    def buscarAutor(self, valor):
        if(valor == None):
            resultado = self.all()
        else:
            resultado = self.filter(
                Q(nombre__icontains = valor) | Q(apellido__icontains = valor)
            ).order_by('apellido', 'nombre')#.exclude(y lo mismo) o filter( Q(edad = 18) | Q(edad = 50) )
        return resultado

    def buscarAutorEdad(self, valor):
        if(valor == None):
            resultado = self.all()
        else:
            resultado = self.filter(
                Q(nombre__icontains = valor) | Q(apellido__icontains = valor)#la , es un and
            ).filter( edad__gt=18 , edad__lt=60 )#exclude(lo mismo pero para negar)
        return resultado
