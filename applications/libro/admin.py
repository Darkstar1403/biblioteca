from django.contrib import admin

# Register your models here.
from .models import Libro, Categoria


class LibroAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'categoria',
        'fecha',
        'visitas',
    )
    search_fields = ('titulo','autor')
    list_filter = ('categoria',)
    filter_horizontal = ('autor',)

admin.site.register(Libro, LibroAdmin)

admin.site.register(Categoria)