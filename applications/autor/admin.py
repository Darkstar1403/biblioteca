from django.contrib import admin

# Register your models here

from .models import Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'nacionalidad',
        'edad',
        'full_name',
    )
    def full_name(self,obj):
        nombreCompleto = obj.nombre + ' ' + obj.apellido
        return nombreCompleto
    search_fields = ('nombre','apellido')
    list_filter = ('nacionalidad','apellido')

admin.site.register(Autor, AutorAdmin)
