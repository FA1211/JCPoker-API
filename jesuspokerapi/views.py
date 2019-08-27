from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Player, Session, SessionResult
from .serializers import PlayerSerializer, SessionSerializer, SessionResultSerializer, PlayerScoreSerializer


# Create your views here.

class PlayerView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request, pk=None, company_pk=None, project_pk=None):
        is_many = True if isinstance(request.data, list) else False

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SessionView(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def create(self, request, *args, **kwargs):
        date = {"date": request.data['date']}
        request.data.pop('date')
        players = request.data

        serializer = self.get_serializer(data=date)
        serializer.is_valid(raise_exception=True)
        sess = serializer.save()

        for player_name, scr in players.items():
            plyr, created = Player.objects.get_or_create(name=player_name)
            result = SessionResult.objects.create(player=plyr, result=int(scr), session=sess)
            result.save()
            plyr.save()
            sess.players.add(plyr)
            sess.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SessionResultView(viewsets.ModelViewSet):
    queryset = SessionResult.objects.all()
    serializer_class = SessionResultSerializer

    def create(self, request, pk=None, company_pk=None, project_pk=None):
        is_many = True if isinstance(request.data, list) else False

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AllScoresView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerScoreSerializer
    sessions = SessionSerializer

