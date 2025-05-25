from rest_framework import generics

from ..models import Post
from ..serializers import PostSerializer

class ListarPosts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditarPosts(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Post.objects.all().order_by("created_at")