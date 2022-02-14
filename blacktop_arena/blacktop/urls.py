from django.urls import path
from .import views
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('team/', views.GetAllTeams.as_view()),
    path('team/create', views.CreateTeam.as_view()),
    path('team/<int:pk>', views.GetTeamById.as_view()),
    path('team/update/<int:pk>', views.UpdateTeamById.as_view()),
    path('players/', views.GetAllPlayers.as_view()),
    path('players/<int:pk>', views.GetPlayerById.as_view()),
    path('games/<int:pk>', views.GetGameById.as_view()),
    path('games/', views.GetAllGames.as_view()),
    path('games/', views.CreateGame.as_view()),
    path('team/<str:team_name>/<str:password>', views.GetTeamByNameAndPassword.as_view()),
    path('squad/<str:team_name>', views.GetSquadByName.as_view()),
    path('squad/<int:pk>/update', views.UpdateSquadById.as_view()),
    path('squad/', views.GetAllSquads.as_view()),
    


]
