from django.urls import path
from categorias import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listar/', views.ListaCategoriasView.as_view(), name='listar_categorias'),
    path('crear/', views.CrearCategoriaView.as_view(), name='crear_categoria'),    
]
