from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from blog.models import Post, Author


# Create your views here.

class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Tomar solo los campos 'title' y 'date' de todos los posts
        posts = Post.objects.values('title', 'date')
        context['posts'] = posts[:5]
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    

class PostCreateView(CreateView):
    template_name = 'blog/post_new.html'
    model = Post
    fields = '__all__'
    success_url = '/post/list/'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return super().get_context_data(**kwargs)
    

class AuthorCreateView(CreateView):
    template_name = 'blog/author_new.html'
    model = Author
    fields = '__all__'
    success_url = '/author/list/'
    
    
class AuthorListView(ListView):
    model = Author
    template_name = 'blog/author_list.html'
    context_object_name = 'authors'
    

class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'blog/author_new.html'
    success_url = '/author/list/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Author edit...'
        return super().get_context_data(**kwargs)