from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'cover', 'name', 'following', 'followers']

    def get_following(self, obj):
        return [profile.user.username for profile in obj.following.all()]

    def get_followers(self, obj):
        return [profile.user.username for profile in obj.followers.all()]