from rest_framework import serializers
from django.contrib.auth.models import User
from .profile_serializer import ProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']
        read_only_fields = ['id', 'username', 'email']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})

        # Atualiza o próprio usuário
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Atualiza o perfil relacionado
        profile = instance.profile
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance
