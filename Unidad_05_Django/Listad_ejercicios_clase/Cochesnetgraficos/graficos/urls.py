from django.urls import path, include
from graficos import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', view=views.index, name='index'),
    path('sectores', view=views.sectores, name='sectores'),
    path('barras', view=views.barras, name='barras'),
    path('lineas', view=views.lineas, name='lineas'),
]