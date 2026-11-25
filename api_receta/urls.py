from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet, basename='categoria')
router.register(r'recetas', views.RecetaViewSet, basename='receta')

urlpatterns = [
    path('recetas/', views.RecetaListView.as_view(), name='listado_recetas'),
    path('recetas/crear/', views.RecetaCreateView.as_view(), name='crear_receta'),
    path('recetas/<int:pk>/', views.RecetaDetailView.as_view(), name='detalle_receta'),
    path('recetas/editar/<int:pk>/', views.RecetaUpdateView.as_view(), name='editar_receta'),
    path('recetas/eliminar/<int:pk>/', views.RecetaDeleteView.as_view(), name='eliminar_receta'),

    # CRUD Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='listado_categorias'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='detalle_categoria'),
    path('categorias/editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),

    path('api/', include(router.urls)),
]