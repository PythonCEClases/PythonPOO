from django.urls import path, include
from recetas import views

urlpatterns = [
    path('', view= views.index, name= 'index'),
    path('list/', view=views.recetas_listado, name= 'recetas_list'),
    path('autor/', view=views.recetas_autor, name= 'recetas_autor'),
    path('contacto/', view=views.recetas_contacto, name= 'recetas_contacto'),
]