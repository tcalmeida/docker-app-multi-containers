from django.urls import path
from .views import game_list, create_game, game_detail, update_game, delete_game

urlpatterns = [
    path('game-list/', game_list, name='game-list'),
    path('game-create/', create_game, name='create-game'),
    path('list-game/<str:pk>/', game_detail, name='list-game'),
    path('update-game/<str:pk>/', update_game, name='update-game'),
    path('delete-game/<str:pk>/', delete_game, name='delete-game'),
]
