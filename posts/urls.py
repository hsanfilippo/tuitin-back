from django.urls import path

from .viewsets import ListarCriarPosts, EditarExcluirPosts, ComentarioCreateList
from .viewsets.post_viewset import toggle_like

urlpatterns = [
    path('posts/', ListarCriarPosts.as_view(), name="listar-posts"),
    path('posts/<uuid:id>/', EditarExcluirPosts.as_view(), name="editar-excluir-posts"),
    path('posts/<uuid:post_id>/toggle_like/', toggle_like, name='toggle-like'),
    path('comentarios/', ComentarioCreateList.as_view(), name='list-create-comentarios'),
]
