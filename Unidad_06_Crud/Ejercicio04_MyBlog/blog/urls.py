from django.urls import path, include
from blog.views import PostListView, IndexView, PostCreateView, AuthorCreateView, AuthorListView, AuthorUpdateView

urlpatterns = [
    path('', view=IndexView.as_view(), name='index'),
    path('post/list/', view=PostListView.as_view(), name='post_list'),
    path('post/new/', view=PostCreateView.as_view(), name='new_post'),
    path('author/new/', view=AuthorCreateView.as_view(), name='new_author'),
    path('author/list/', view=AuthorListView.as_view(), name='author_list'),
    path('author/edit/<int:pk>/', view=AuthorUpdateView.as_view(), name='edit_author'),
]