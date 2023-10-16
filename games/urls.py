from django.urls import path
from .views import game_list

urlpatterns = [
    path('game-list/', game_list, name='game-list')
]
