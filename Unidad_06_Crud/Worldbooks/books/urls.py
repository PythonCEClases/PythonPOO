from django.urls import path
from books import views

urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),
    path('list/', view=views.ListBookView.as_view(), name='list_books'),
    path('new/', view=views.NewBookView.as_view(), name='new_book'),
    path('edit/<int:pk>/', view=views.EditBookView.as_view(), name='edit_book'),
    path('delete/<int:pk>/', view=views.DeleteBookView.as_view(), name='delete_book'),
]