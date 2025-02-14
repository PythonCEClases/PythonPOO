from django.views.generic import ListView, \
    TemplateView, CreateView, UpdateView, DeleteView
from django import forms
from books.models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.

class IndexView(TemplateView):
    template_name = 'books/index.html'
    
    
class ListBookView(ListView):
    model = Book
    template_name = 'books/list_books.html'
    context_object_name = 'books'    
    

class NewBookView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/new_book.html'
    fields = ['title', 'author', 'price', 'publisher', 'release_date', 'cover']
    success_url = '/list/'
    
    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'New book'
        return context
    
class EditBookView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/edit_book.html'
    fields = ['title', 'author', 'price', 'publisher', 'release_date', 'cover']
    success_url = '/list/'
    
    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'Edit a book'
        return context
    
class DeleteBookView(DeleteView):
    model = Book
    template_name = 'books/delete_book.html'
    success_url = '/list/'
    
class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')
    # fields = ['username', 'password']
    
    def form_valid(self, form):
        form.save()
        # return super().form_valid(form)
        return redirect(self.success_url)
    
    
    
    
    