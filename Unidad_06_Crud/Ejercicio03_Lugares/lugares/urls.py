from django.urls import path
from lugares import views

urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),   
    path('listar/', view=views.ListaLugaresView.as_view(), name='listar_lugares'),
    path('nuevo/', view=views.NuevoLugarView.as_view(), name='nuevo_lugar'),
    path('detaller/<int:pk>/', view=views.DetalleLugarView.as_view(), name='detalle_lugar'),
]
