from rest_framework import serializers
from .models import Player, User


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'nickname', 'height', 'attributes', 'tendencies','avatar','description')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'wins', 'losses')
