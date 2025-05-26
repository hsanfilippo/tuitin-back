from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from ..models import Profile

User = get_user_model()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, username):
    try:
        me = request.user.profile
        target = Profile.objects.get(user__username=username)

        if me == target:
            return Response({'error': 'Você não pode seguir você mesmo.'}, status=status.HTTP_400_BAD_REQUEST)

        me.following.add(target)
        return Response({'success': f'Seguindo {username}'}, status=status.HTTP_200_OK)

    except Profile.DoesNotExist:
        return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, username):
    try:
        me = request.user.profile
        target = Profile.objects.get(user__username=username)

        if me == target:
            return Response({'error': 'Você não pode deixar de seguir a si mesmo.'}, status=status.HTTP_400_BAD_REQUEST)

        me.following.remove(target)
        return Response({'success': f'Parou de seguir {username}.'}, status=status.HTTP_200_OK)

    except Profile.DoesNotExist:
        return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)