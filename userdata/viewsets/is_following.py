from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from ..models import Profile

class IsFollowingViewset(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        target_profile = get_object_or_404(Profile, user__username=username)

        # O usuário autenticado (request.user) também tem um profile
        current_user_profile = request.user.profile

        # Verificamos se o profile atual está seguindo o target
        is_following = target_profile in current_user_profile.following.all()

        return Response({"is_following": is_following})
