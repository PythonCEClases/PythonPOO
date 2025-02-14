from django.views.generic import ListView, \
    TemplateView, CreateView, UpdateView, DeleteView
from django import forms
from books.models import Book

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    
    
class ListBookView(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'    
    
    
class NewBookView(CreateView):
    model = Book
    template_name = 'new_book.html'
    fields = ['title', 'author', 'price', 'publisher', 'release_date']
    success_url = '/list/'
    
    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rotulo'] = 'New book'
        return context
    
class EditBookView(UpdateView):
    model = Book
    template_name = 'new_book.html'
    fields = ['title', 'author', 'price', 'publisher', 'release_date']
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
    template_name = 'delete_book.html'    
    success_url = '/list/'
    
    