from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
from .serializers import PlayerSerializer, UserSerializer
from .models import Player, User

# Create your views here.


class GetAllPlayers(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GetPlayerById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GetUserById(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = PlayerSerializer


# class GetPlayerById(APIView):
#     queryset = Player.objects.all()

#     def post(self, request, format=None):
#         player_pk = int(request.data.get('player')) or None

#         player = self.queryset.filter(id=player_pk).first()

#         if player == None:
#             return Response('Failed!')

#         serializer = PlayerSerializer(player)
#         print(serializer.data)
#         player_info = {
#             'name': serializer.data['name'],
#             'nickname': serializer.data['nickname'],
#             'height': serializer.data['height'],
#             'attributes': serializer.data['attributes'],
#             'tendencies': serializer.data['tendencies'],
#             'avatar': serializer.data['avatar'],
#             'description': serializer.data['description']
#         }

#         return Response(player_info)
