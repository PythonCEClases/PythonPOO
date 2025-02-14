from django.urls import path    
from cursos import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),    
    path('listestudiantes/', views.ListEstudiantesView.as_view(), name='estudiantes_list'),
    # path('listcursos/', views.ListCursosView.as_view(), name='cursos_list'),
    
    path('detail/estudiante/<int:pk>/', views.EditarEstudianteView.as_view(), name='editar_estudiante'),  
          
    path('cursos/estudiante/<int:pk>/', views.CursosEstudianteView.as_view(), name='cursos_estudiante'),
    
    path('nuevoestudiante/', views.NuevoEstudianteView.as_view(), name='nuevo_estudiante'),
    
    path('estudiante/<int:estudiante_id>/eliminar_curso/<int:curso_id>/', views.EliminarCursoEstudianteView.as_view(), 
         name='eliminar_curso_estudiante'),
    
]