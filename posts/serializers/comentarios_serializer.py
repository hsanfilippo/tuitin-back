from rest_framework import serializers
from ..models import Comentarios

class ComentariosSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comentarios
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at']
        read_only_fields = ['author', 'created_at']
