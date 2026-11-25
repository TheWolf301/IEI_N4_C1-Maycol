from django import forms
from .models import Receta, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Postres, Comida Chilena, Ensaladas'
            }),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'titulo',
            'categoria',
            'tiempo_preparacion',
            'porciones',
            'ingredientes',
            'preparacion',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título de la receta'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tiempo_preparacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tiempo en minutos (ej: 45)',
                'min': 1
            }),
            'porciones': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de porciones (ej: 4)',
                'min': 1
            }),
            'ingredientes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Liste los ingredientes necesarios'
            }),
            'preparacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describa paso a paso la preparación'
            }),
        }