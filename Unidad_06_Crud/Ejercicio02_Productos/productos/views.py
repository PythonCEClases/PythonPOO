from django.shortcuts import render
from django.views.generic import ListView, CreateView
from productos.models import Producto
from django.urls import reverse_lazy
from categorias.models import Categoria
from productos.forms import ProductoForm

# Create your views here.

class ListaProductosView(ListView):
    model = Producto
    template_name = 'productos/lista_productos.html'
    context_object_name = 'productos'
    paginate_by = 10
    
    
class CrearProductoView(CreateView):
    model = Producto
    # form_class = ProductoForm
    fields = '__all__'
    template_name = 'productos/crear_producto.html'    
    success_url = reverse_lazy('listar_productos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return super().get_context_data(**kwargs)