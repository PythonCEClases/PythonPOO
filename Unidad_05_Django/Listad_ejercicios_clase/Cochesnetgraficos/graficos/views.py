from django.shortcuts import render
from graficos.models import Marca, Coche
from functools import reduce
import plotly.express as px
from django.db.models import Avg

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sectores(request):
    
    # obtener los datos de la base de datos
    marcas = Marca.objects.values_list('nombre').distinct() 
    marcas_list = list(reduce(lambda x, y: x + y, marcas))
    cuentas = [Coche.objects.filter(marca__nombre=marca[0]).count() for marca in marcas]
    
    fig = px.pie(values=cuentas, names=marcas_list, title='Nº de coches por marca')
    
    chart = fig.to_html(full_html=False)
    context = {
        'chart': chart
    }

    return render(request, 'sectores.html', context)


def barras(request):
    
    # obtener los datos de la base de datos
    # precio medio x marca
    marcas = Marca.objects.values_list('nombre').distinct() 
    values = [
        Coche.objects.filter(marca__nombre=marca[0]).aggregate(Avg('precio'))['precio__avg'] for marca in marcas
    ]
    marcas_list = list(reduce(lambda x, y: x + y, marcas))
    
    fig = px.bar(x=marcas_list, y=values, title="Precio medio por marca")
    chart = fig.to_html(full_html=False)
    context = {
        'chart': chart
    }
    
    return render(request, 'barras.html', context)
    


def lineas(request):
    
    # obtener los datos de la base de datos
    # Año de fabricación y nº coches
    
    anios = [x for x in range(2010, 2025)]
    cuenta_por_anio = [Coche.objects.filter(fecha_fabricacion__year=year).count() for year in anios]
    
    fig = px.line(x=anios, y=cuenta_por_anio)
    chart = fig.to_html(full_html=False)
    context = {
        'chart': chart
    }
    
    
    fir = px.line(x=anios, y=cuenta_por_anio, title="Nº coches x año de fabricación")
    chart = fir.to_html(full_html=False)
    context = {
        'chart': chart
    }
    
    return render(request, 'lineas.html', context)