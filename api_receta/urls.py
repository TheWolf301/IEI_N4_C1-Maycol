from django.urls import path, include
from rest_framework import routers
from api_receta import views

enrutador = routers.DefaultRouter()
enrutador.register(r'categorias', views.CategoriaViewSet)
enrutador.register(r'recetas', views.RecetaViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]