from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from cursos.models import Estudiante
from cursos.forms import NuevoEstudianteForm



class IndexView(TemplateView):
    template_name = 'index.html'
    

class ListEstudiantesView(ListView):
    template_name = 'listar_estudiantes.html'
    model = Estudiante
    context_object_name = 'estudiantes'
    

class CursosEstudianteView(DetailView):
    model = Estudiante
    template_name = "cursos_estudiante.html"
    context_object_name = "estudiante"
    

class NuevoEstudianteView(FormView):
    template_name = 'nuevo_estudiante.html'
    success_url = '/listestudiantes/'
    form_class = NuevoEstudianteForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'Nuevo estudiante'
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class EditarEstudianteView(FormView):
    template_name = 'nuevo_estudiante.html'
    success_url = '/listestudiantes/'
    form_class = NuevoEstudianteForm
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        estudiante = Estudiante.objects.get(pk=self.kwargs['pk'])
        kwargs['instance'] = estudiante
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'Editar estudiante'
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class EliminarCursoEstudianteView(View):
        
    def get(self, request, estudiante_id, curso_id):
        estudiante = Estudiante.objects.get(pk=estudiante_id)
        estudiante.cursos.remove(curso_id)
        print(estudiante.id)
        print(curso_id)
        
        return redirect(reverse_lazy('estudiantes_list'))
    