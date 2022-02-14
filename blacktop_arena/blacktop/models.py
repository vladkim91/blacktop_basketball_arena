from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name


class Game(models.Model):
    name = models.CharField(max_length=10, default="game_name")
    team_one_stats = models.JSONField(default=dict)
    team_two_stats = models.JSONField(default=dict)
    team_one_player_stats = models.JSONField(default=dict)
    team_two_player_stats = models.JSONField(default=dict)
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)
    team_one_squad = models.JSONField(default=dict)
    team_two_squad = models.JSONField(default=dict)
    date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    height = models.IntegerField()
    attributes = models.JSONField(default=dict)
    tendencies = models.JSONField(default=dict)
    avatar = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=500)
    tier = models.IntegerField()

    def __str__(self):
        return self.name


class Squad(models.Model):
    team_name = models.CharField(max_length=100)
    players = models.JSONField(default=dict)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name
