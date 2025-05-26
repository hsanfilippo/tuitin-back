from django.urls import path
from .viewsets import RegisterUsers, MeViewset, PublicUserViewset
from .viewsets.follow import follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterUsers.as_view(), name='register'),
    path('me/', MeViewset.as_view(), name='me'),
    path('users/<str:username>/', PublicUserViewset.as_view(), name='public-users-list'),
    path('users/<str:username>/follow/', follow_user, name='follow-user'),
    path('users/<str:username>/unfollow/', unfollow_user, name='unfollow-user')
]
