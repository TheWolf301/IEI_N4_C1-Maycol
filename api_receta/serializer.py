from rest_framework import serializers

from .models import Receta
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class RecetaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = 'titulo', 'categoria', 'tiempo_preparacion', 'porciones'