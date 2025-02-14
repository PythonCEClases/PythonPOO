from django.urls import path, include
from agenda import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', view=views.index, name='index'),
    path('listar/', view=views.ListaContactosView.as_view(), name='listar_contactos'),
    path('nuevo/', view=views.NuevoContactoView.as_view(), name='nuevo_contacto'),
    
    path('editar/<int:pk>/', view=views.UpdateContactoView.as_view(), name='editar_contacto'),
    
    
    path('eliminar/<int:pk>/', view=views.DeleteContactoView.as_view(), name='eliminar_contacto'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)