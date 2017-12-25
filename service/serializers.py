from django.contrib.auth.models import User
from rest_framework import serializers

from service.models import Playlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name')

class PlaylistSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True, default=serializers.CurrentUserDefault)

    class Meta:
        model = Playlist
        fields = ('id', 'name', 'videos')