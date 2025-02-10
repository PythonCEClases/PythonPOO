from django.shortcuts import render
from coches.models import Coche, Marca
import random

# Create your views here.


def index(request):
    return render(request, "index.html")


def todos(request):
    todos = Coche.objects.all()
    return render(request, "todos.html", context={"coches": todos})


def marcas(request):
    marcas = Marca.objects.all()
    return render(request, "marcas.html", context={"marcas": marcas})


def marca_por_id(request, id):
    # Buscar la marca con el id que viene en la URL
    marca = Marca.objects.get(pk=id)
    # Acceder a todos los coches de esa marca
    coches = marca.coche_set.all()
    # Enviar los coches a la plantilla
    return render(request, "todos.html", context={"coches": coches})
