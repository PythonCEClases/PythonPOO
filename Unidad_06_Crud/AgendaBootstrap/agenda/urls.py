from django.urls import path, include
from agenda import views


urlpatterns = [
    path('', view=views.index, name='index'),
    path('listar/', view=views.ListaContactosView.as_view(), name='listar_contactos'),
    path('nuevo/', view=views.NuevoContactoView.as_view(), name='nuevo_contacto'),    
    path('editar/<int:pk>/', view=views.UpdateContactoView.as_view(), name='editar_contacto'),
    path('eliminar/<int:pk>/', view=views.DeleteContactoView.as_view(), name='eliminar_contacto'),
]