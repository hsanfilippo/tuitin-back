from rest_framework import serializers
from django.contrib.auth import get_user_model

from .profile_serializer import ProfileSerializer

User = get_user_model()


class PublicUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'profile']