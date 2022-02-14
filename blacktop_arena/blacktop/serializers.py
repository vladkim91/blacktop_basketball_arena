from rest_framework import serializers
from .models import Player, Team, Game, Squad


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

    class Meta:
        model = Game
        fields = ('id', 'team_one_stats', 'team_one_score', 'team_one_player_stats',
                  'team_one_squad', 'team_two_stats', 'team_two_score', 'team_two_player_stats', 'team_two_squad', 'date')


class SquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squad
        fields = ('id', 'team_name', 'players', 'wins', 'losses')
