from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
class GameList(APIView):
    pass
@api_view(['GET'])
def overview(request):
    context = {'Hello': 'World'}
    return Response(context)