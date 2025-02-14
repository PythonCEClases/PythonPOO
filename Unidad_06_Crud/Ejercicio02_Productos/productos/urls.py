from django.urls import path
from productos import views

urlpatterns = [
    path('listar/', views.ListaProductosView.as_view(), name='listar_productos'),
    path('crear/', views.CrearProductoView.as_view(), name='crear_producto'),  
]
