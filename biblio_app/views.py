from django.shortcuts import render

def home(request):
    recetas_destacadas = [
        {"id": 1, "titulo": "Pasta Carbonara Tradicional", "tiempo": "25 min", "dificultad": "Fácil", "categoria": "Italiana"},
        {"id": 2, "titulo": "Tacos al Pastor", "tiempo": "40 min", "dificultad": "Intermedia", "categoria": "Mexicana"},
        {"id": 3, "titulo": "Ceviche de Pescado", "tiempo": "20 min", "dificultad": "Fácil", "categoria": "Marina"},
    ]
    return render(request, 'index.html', {'recetas': recetas_destacadas})

def lista_recetas(request):
    return render(request, 'recetas.html')