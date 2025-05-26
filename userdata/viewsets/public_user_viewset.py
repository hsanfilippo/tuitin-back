from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from ..serializers import PublicUserSerializer

User = get_user_model()


class PublicUserViewset(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = PublicUserSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'username'