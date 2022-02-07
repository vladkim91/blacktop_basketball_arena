from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Game(models.Model):
    stats = models.JSONField("stats")
    winner = models.ForeignKey(
        User, related_name='winner', null=True, default=None, on_delete=models.CASCADE, blank=True
    )
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
    current_team = models.ForeignKey(
        User, related_name='current_team', null=True, default=None, on_delete=models.PROTECT
    )
    user_team = models.ForeignKey(
        Game, related_name='user_team', null=True, default=None, on_delete=models.PROTECT
    )
    cpu_team = models.ForeignKey(
        Game, related_name='cpu_team', null=True, default=None, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

