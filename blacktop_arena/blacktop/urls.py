from django.urls import path
from .import views

urlpatterns = [

  path('user/<int:pk>', views.GetUserById.as_view()),
  path('players/', views.GetAllPlayers.as_view()),
  path('players/<int:pk>', views.GetPlayerById.as_view()),
]