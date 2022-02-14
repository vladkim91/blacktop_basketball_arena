from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from .serializers import PlayerSerializer, TeamSerializer, GameSerializer, SquadSerializer
from .models import Player, Team, Game, Squad
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class GetGameById(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GetAllGames(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CreateGame(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GetTeamById(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CreateTeam(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class GetAllPlayers(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GetPlayerById(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GetAllTeams(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UpdateTeamById(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class GetTeamByNameAndPassword(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'team_name'


class GetSquadByName(generics.RetrieveAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer
    lookup_field = 'team_name'


class UpdateSquadById(generics.UpdateAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer

class GetAllSquads(generics.ListCreateAPIView):
    queryset = Squad.objects.all()
    serializer_class = SquadSerializer