from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    ingredientes = models.TextField(null=False)
    preparacion = models.TextField(null=False)
    tiempo_preparacion = models.IntegerField(null=False)
    porciones = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo