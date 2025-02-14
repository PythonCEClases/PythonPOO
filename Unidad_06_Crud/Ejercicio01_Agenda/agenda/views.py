from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from agenda.models import Contacto

# Create your views here.

def index(request):
    return render(request, 'index.html')


class ListaContactosView(ListView):
    model = Contacto
    template_name = 'listar_contactos.html'
    context_object_name = 'contactos'    
    

class NuevoContactoView(CreateView):
    model = Contacto
    fields = ['nombre', 'apellidos', 'telefono', 'email', 'direccion', 'localidad']
    template_name = 'nuevo_contacto.html'
    success_url = '/listar/'


class DeleteContactoView(DeleteView):
    model = Contacto
    success_url = '/listar/'
    template_name = 'confirmar_delete.html'
    

class UpdateContactoView(UpdateView):
    model = Contacto
    template_name = 'nuevo_contacto.html'
    fields = ['nombre', 'apellidos', 'telefono', 'email', 'direccion', 'localidad']
    success_url = '/listar/'
    
    

