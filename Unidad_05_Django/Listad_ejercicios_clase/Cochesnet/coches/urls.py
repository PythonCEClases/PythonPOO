from django.urls import include, path

from coches import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("todos/", view=views.todos, name="todos"),
    path("marcas/", view=views.marcas, name="marcas"),
    path("marca/<int:id>/", view=views.marca_por_id, name="marca_por_id"),
]
