from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer


# list all games
@api_view(['GET'])
def game_list(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_game(request):
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
