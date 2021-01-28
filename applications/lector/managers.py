from django.db import models
from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):

    def librosPromedioEdad(self):
        resultado = self.filter(
            libro__id = '1'
        ).aggregate(
            promedioEdad = Avg('lector__edad'),
            sumaEdad= Sum('lector__edad')
        )
        return resultado

    def numLibrosPrestados(self):
        resultado = self.values(
            'libro'
            #,'lector'
        ).annotate(
            numPrestados = Count('libro'),
            titulo=Lower('libro__titulo'),
        )

        for r in resultado:
            print(r, r['numPrestados'])
        return resultado