from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Player, Session, SessionResult


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name')


class SessionResultSerializer(serializers.ModelSerializer):
    player = StringRelatedField(many=False)

    class Meta:
        model = SessionResult
        fields = ('id', 'session', 'player', 'result')


class SessionSerializer(serializers.ModelSerializer):
    results = SessionResultSerializer(many=True)

    class Meta:
        model = Session
        fields = ('id', 'date', 'results', 'balance')