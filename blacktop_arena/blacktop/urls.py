from django.urls import path
from .import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('user/create', views.CreateUser.as_view()),
    path('user/<int:pk>', views.GetUserById.as_view()),
    path('players/', views.GetAllPlayers.as_view()),
    path('players/<int:pk>', views.GetPlayerById.as_view()),
    path('games/<int:pk>', views.GetGameById.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
