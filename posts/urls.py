from django.urls import path

from .viewsets import ListarCriarPosts, EditarExcluirPosts

urlpatterns = [
    path('posts/', ListarCriarPosts.as_view(), name="listar-posts"),
    path('posts/<uuid:id>/', EditarExcluirPosts.as_view(), name="editar-excluir-posts")
]
