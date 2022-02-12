from rest_framework import serializers
from .models import Player, Team, Game


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'nickname', 'height', 'attributes',
                  'tendencies', 'avatar', 'description', 'image', 'tier')


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'password', 'wins', 'losses')


class GameSerializer(serializers.ModelSerializer):

    winner_list = TeamSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Game
        fields = ('id', 'game_stats', 'winner_list', 'winner', 'team_one_stats', 'team_one_score', 'team_one',
                  'team_one_squad', 'team_two_stats', 'team_two_score', 'team_two', 'team_two_squad', 'date')

