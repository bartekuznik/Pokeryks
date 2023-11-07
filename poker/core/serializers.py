from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password'
        ]

class ExtendUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendUser
        fields=[
            'coin_numbers',
            'is_vip',
            'user',
        ]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            '__all__'
        ]

class PlayerGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerGame
        fields = [
            '__all__'
        ]

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = [
            '__all__'
        ]
