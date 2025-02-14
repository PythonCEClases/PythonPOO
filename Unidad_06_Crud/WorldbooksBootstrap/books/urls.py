from django.urls import path
from books import views
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),
    path('list/', view=views.ListBookView.as_view(), name='list_books'),
    path('new/', view=views.NewBookView.as_view(), name='new_book'),
    path('edit/<int:pk>/', view=views.EditBookView.as_view(), name='edit_book'),
    path('delete/<int:pk>/', view=views.DeleteBookView.as_view(), name='delete_book'),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', view=views.RegisterView.as_view(), name='register'),
    
    path('registro/', views.RegistroView.as_view()  , name='registro'),
    
] 