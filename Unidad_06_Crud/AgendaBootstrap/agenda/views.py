from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from agenda.models import Contacto
from agenda.forms import ContactoForm
from django import forms

# Create your views here.

def index(request):
    return render(request, 'index.html')


class ListaContactosView(ListView):
    model = Contacto
    template_name = 'listar_contactos.html'
    context_object_name = 'contactos'    
    

class NuevoContactoView(CreateView):
    model = Contacto
    # form_class = ContactoForm
    fields = ['nombre', 'apellidos', 'telefono', 'email', 'direccion', 'localidad']
    template_name = 'nuevo_contacto.html'
    success_url = '/listar/'
    
    def get_context_data(self, **kwargs):        
        # Mostrar el texto 'Crear' en vez de 'Editar'
        contexto = super().get_context_data(**kwargs)
        contexto['accion'] = 'Crear'
        return contexto

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['direccion'].widget = forms.TextInput(attrs={'type': 'text'})
        return form

class DeleteContactoView(DeleteView):
    model = Contacto
    success_url = '/listar/'
    template_name = 'confirmar_delete.html'
    

class UpdateContactoView(UpdateView):
    model = Contacto
    template_name = 'nuevo_contacto.html'
    fields = ['nombre', 'apellidos', 'telefono', 'email', 'direccion', 'localidad']
    success_url = '/listar/'
    
    def get_context_data(self, **kwargs):        
        # Mostrar el texto 'Editar' en vez de 'Crear'
        contexto = super().get_context_data(**kwargs)
        contexto['accion'] = 'Editar'
        return contexto
    
    def get_form(self, form_class=None):
          # Para que el campo direccion sea un input de tipo texto y no un textarea
        form = super().get_form(form_class)
        form.fields['direccion'].widget = forms.TextInput(attrs={'type': 'text'})
        return form