from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=40, blank=True, default='')
    avatar = models.TextField(blank=True, default='')
    cover = models.TextField(blank=True, default='')
    bio = models.TextField(blank=True, default='')
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
