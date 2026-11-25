from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .models import Receta, Categoria
from .serializers import RecetaSerializer, CategoriaSerializer
from .forms import RecetaForm, CategoriaForm

def index(request):
    return render(request, 'index.html')

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class RecetaListView(ListView):
    model = Receta
    template_name = 'receta/listado_recetas.html'
    context_object_name = 'recetas'

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'receta/detalle_receta.html'
    context_object_name = 'receta'

class RecetaCreateView(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'receta/crear_receta.html'
    success_url = reverse_lazy('listado_recetas')

class RecetaUpdateView(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'receta/editar_receta.html'
    success_url = reverse_lazy('listado_recetas')

class RecetaDeleteView(DeleteView):
    model = Receta
    template_name = 'receta/eliminar_receta.html'
    context_object_name = 'receta'
    success_url = reverse_lazy('listado_recetas')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listado_categorias.html'
    context_object_name = 'categorias'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria/detalle_categoria.html'
    context_object_name = 'categoria'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear_categoria.html'
    success_url = reverse_lazy('listado_categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/editar_categoria.html'
    success_url = reverse_lazy('listado_categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/eliminar_categoria.html'
    context_object_name = 'categoria'
    success_url = reverse_lazy('listado_categorias')