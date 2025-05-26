from rest_framework import generics, permissions

from ..models import Post
from ..serializers import PostSerializer

class ListarCriarPosts(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EditarExcluirPosts(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Post.objects.all().order_by("created_at")