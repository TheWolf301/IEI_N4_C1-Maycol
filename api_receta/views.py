from rest_framework import viewsets
from django.shortcuts import render

from .models import Categoria, Receta
from .serializers import CategoriaSerializer, RecetaSerializer

def index(request):
    return render(request, 'index.html')

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer