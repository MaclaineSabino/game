"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer
from datetime import datetime
from django.utils import timezone

@api_view(['GET','POST'])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games,many=True)
        return Response(games_serializer.data)
    elif request.method =='POST':

        valores = dict(request.data)
        jogo3 = Game.objects.filter(name=valores['name'])

        if len(jogo3)>0:
            return Response('já existe um jogo com esse nome',
                        status=status.HTTP_412_PRECONDITION_FAILED)

        else:

            if len(valores)<4:

                return Response('todos os campos devem ser prenchidos',
                        status=status.HTTP_412_PRECONDITION_FAILED)
            else:
                game_serializer = GameSerializer(data=request.data)
                if game_serializer.is_valid():
                  game_serializer.save()
                  return Response(game_serializer.data,
                            status=status.HTTP_201_CREATED)
                return Response(game_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def game_detail(request,pk):
    try:
        game=Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return Response(game_serializer)
    elif request.method == 'PUT':
        valores = dict(request.data)
        jogo3 = Game.objects.filter(name=valores['name'])

        if len(jogo3)>0:
            return Response('já existe um jogo com esse nome',
                        status=status.HTTP_412_PRECONDITION_FAILED)


        else:
             if len(request.data)<4:
                return Response('todos os campos devem ser preenchidos',status=status.HTTP_412_PRECONDITION_FAILED)
             else:
                game_serializer = GameSerializer(game,data=request.data)
                if game_serializer.is_valid():
                    game_serializer.save()
                    return Response(game_serializer.data)
                return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data = timezone.make_aware(datetime.now(),timezone.get_current_timezone())

        if data>game.release_date:

            return Response('esse jogo já foi lançado, somente jogos que ainda não foram lançados podem ser excluidos ',
                        status=status.HTTP_412_PRECONDITION_FAILED)
        else:

            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



