from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from categorias.models import Categoria 

# Create your views here.

class IndexView(TemplateView):
    template_name = 'categorias/index.html'
    

class ListaCategoriasView(ListView):
    model = Categoria
    template_name = 'categorias/lista_categorias.html'
    context_object_name = 'categorias'  
    

class CrearCategoriaView(CreateView):
    model = Categoria
    template_name = 'categorias/crear_categoria.html'
    fields = '__all__'
    success_url = '/categorias/listar'