from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *

# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExtendUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ExtendUserSerializer
    
class ExtendUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ExtendUserSerializer

class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class PlayerList(generics.ListAPIView):
    queryset = PlayerGame.objects.all()
    serializer_class = PlayerGameSerializer
    
class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerGame.objects.all()
    serializer_class = PlayerGameSerializer

class RankList(generics.ListAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    
class RankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer