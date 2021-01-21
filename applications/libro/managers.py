from django.db import models
import datetime

from django.db.models import Q


class LibroManager(models.Manager):
    """Managers para el modelo autor"""

    def listarLibros(self):
       return self.all()

    def buscarLibro(self, valor):
        if(valor == None):
            resultado = self.all()
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