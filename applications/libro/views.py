from django.shortcuts import render

from django.views.generic import ListView, DetailView
# Create your views here.
from applications.libro.models import Libro


class ListLibros(ListView):

    context_object_name = 'libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabraClave = self.request.GET.get('nombre', '')
        fechaInicial = self.request.GET.get('fechaInicio', '')
        fechaFinal = self.request.GET.get('fechaFinal', '')

        if(fechaInicial and fechaFinal):
            return Libro.objects.buscarLibroFecha(palabraClave, fechaInicial, fechaFinal)
        else:
            return Libro.objects.buscarLibro(palabraClave)

class ListLibrosCategoria(ListView):

    context_object_name = 'libros'
    template_name = 'libro/lista_categoria.html'

    def get_queryset(self):

        return Libro.objects.listarLibrosCategoria('1')


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/detalle.html'
