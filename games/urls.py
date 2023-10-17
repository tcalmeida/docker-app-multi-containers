from django.urls import path
from .views import game_list, create_game

urlpatterns = [
    path('game-list/', game_list, name='game-list'),
    path('game-create/', create_game, name='create-game')
]
