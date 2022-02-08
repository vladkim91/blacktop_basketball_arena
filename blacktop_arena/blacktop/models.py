from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Game(models.Model):
    name = models.CharField(max_length=10,default="game_name")
    game_stats = models.JSONField(default=dict)
    winner = models.ForeignKey(
        User, related_name='winner', null=True, default=None, on_delete=models.CASCADE, blank=True
    )
    player_one_stats = models.JSONField(default=dict)
    player_two_stats = models.JSONField(default=dict)
    player_one_score = models.IntegerField(default=0)
    player_two_score = models.IntegerField(default=0)
    player_one = models.ForeignKey(User, related_name='player_one', null=True, default=None, on_delete=models.PROTECT, blank=True)
    player_two = models.ForeignKey(User, related_name='player_two', null=True, default=None, on_delete=models.PROTECT, blank=True)
    player_one_squad = models.JSONField(default=dict)
    player_two_squad = models.JSONField(default=dict)
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
    attributes = models.JSONField("attributes")
    tendencies = models.JSONField("tendencies")
    avatar = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

