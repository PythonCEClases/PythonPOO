from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def recetas_listado(request):
    
    recetas = {
        'Receta 1':  'Tortilla de patatas',
        'Receta 2':  'Paella',
        'Receta 3':  'Fabada',
        'Receta 4':  'Gazpacho',
        'Receta 5':  'Cocido madrileño',
        'Receta 6':  'Tarta de manzana'
    }
    
    return render(request, 'lista_recetas.html', {'las_recetas' : recetas})

def recetas_autor(request):
    datos_autor = {
        'nombre': 'Carlos Arquimaño',
        'pais': 'España',
        'ciudad': 'Zafra',
        'estudios': 'Master en cocina extremeña',
    }
    return render(request, 'autor.html', datos_autor)

def recetas_contacto(request):
    datos_contacto = {
        'telefono': '666 123 456',
        'facebook': 'https://www.facebook.com/carlos.arquimaño',
        'x': 'https://x.com/carlosarquimaño',
        'instagram': 'https://www.instagram.com/carlosarquimaño',
    }
    return render(request, 'contacto.html', datos_contacto)

