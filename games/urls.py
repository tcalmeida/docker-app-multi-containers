from django.urls import path
from games.views import GameList, overview

urlpatterns = [
    path('', overview)
]
