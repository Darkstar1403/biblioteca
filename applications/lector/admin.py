from django.contrib import admin

# Register your models here.

from .models import Lector, Prestamo

class LectorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'nacionalidad',
        'edad',
        'Nombre_Completo',
    )
    def Nombre_Completo(self,obj):
        nombreCompleto = obj.nombre + ' ' + obj.apellido
        return nombreCompleto
    search_fields = ('nombre','apellido')
    list_filter = ('nacionalidad','apellido')

admin.site.register(Lector, LectorAdmin)

class PrestamoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'lector',
        'libro',
        'fecha_prestamo',
        'fecha_devolucion',
        'devuelto',
    )

    search_fields = ('libro','lector')
    list_filter = ('libro','lector')

admin.site.register(Prestamo, PrestamoAdmin)
