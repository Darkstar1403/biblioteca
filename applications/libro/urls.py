from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('librosCategoria/', views.ListLibrosCategoria.as_view(), name='libros-categoria'),
    path('libroDetalle/<pk>/', views.LibroDetailView.as_view(), name='libro-detalle'),
]
