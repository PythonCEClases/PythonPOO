from django.shortcuts import render
from lugares.models import Lugar
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from django import forms

# Create your views here.

class ListaLugaresView(ListView):
    model = Lugar
    template_name = 'listar_lugares.html'
    context_object_name = 'lugares'
    
    
class IndexView(TemplateView):
    template_name = 'index.html'
    

class NuevoLugarView(CreateView):
    model = Lugar
    fields = ['nombre', 'descripcion', 'pais', 'localizacion', 'tipo', 'imagen']
    template_name = 'nuevo_lugar.html'
    success_url = '/listar/'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['descripcion'].widget = forms.TextInput(attrs={'type': 'text'})
        return form
    
class DetalleLugarView(DetailView):
    model = Lugar
    template_name = 'detalle_lugar.html'
    context_object_name = 'lugar'
    
    