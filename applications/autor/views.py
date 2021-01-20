from django.shortcuts import render

from django.views.generic import ListView
# Create your views here.
from applications.autor.models import Autor


class ListAutores(ListView):

    context_object_name = 'autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):

        return Autor.objects.listarAutores()