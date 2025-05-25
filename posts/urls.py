from django.urls import path

from .viewsets import ListarPosts, EditarPosts

urlpatterns = [
    path('posts/', ListarPosts.as_view(), name="listar-posts"),
    path('posts/<uuid:id>', EditarPosts.as_view(), name="editar-excluir-posts")
]
