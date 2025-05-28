from rest_framework import serializers
from posts.models.post import Post
from posts.serializers.comentarios_serializer import ComentariosSerializer


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_avatar = serializers.CharField(source='author.profile.avatar', read_only=True)
    author_name = serializers.CharField(source='author.profile.name', read_only=True)
    comentarios = ComentariosSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'created_at', 'like_count', 'comentarios']
