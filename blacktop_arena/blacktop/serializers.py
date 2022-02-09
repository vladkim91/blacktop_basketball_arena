from rest_framework import serializers
from .models import Player, User, Game


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'nickname', 'height', 'attributes', 'tendencies','avatar','description')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'wins', 'losses')

class GameSerializer(serializers.ModelSerializer):

    winner_list = UserSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Game
        fields = ('id', 'game_stats', 'winner_list','winner', 'player_one_stats', 'player_one_score','player_one','player_one_squad','player_two_stats', 'player_two_score','player_two','player_two_squad', 'date')