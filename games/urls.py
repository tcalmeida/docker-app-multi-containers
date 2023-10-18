from django.urls import path
from .views import list_games, list_game, create_game, update_game, delete_game

urlpatterns = [
    path('games-list/', list_games, name='games-list'),
    path('list-game/<str:pk>/', list_game, name='list-game'),
    path('game-create/', create_game, name='create-game'),
    path('update-game/<str:pk>/', update_game, name='update-game'),
    path('delete-game/<str:pk>/', delete_game, name='delete-game'),
]
