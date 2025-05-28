from rest_framework import generics, permissions
from ..models import Comentarios
from ..serializers import ComentariosSerializer

class ComentarioCreateList(generics.ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)