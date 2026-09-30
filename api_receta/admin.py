from django.contrib import admin
from .models import Categoria, Receta

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'created_at')
    search_fields = ('nombre',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria', 'tiempo_preparacion', 'porciones', 'created_at')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'ingredientes')