from django.urls import path
from .viewsets import RegisterUsers, MeViewset

urlpatterns = [
    path('register/', RegisterUsers.as_view(), name='register'),
    path('me/', MeViewset.as_view(), name='me')
]
