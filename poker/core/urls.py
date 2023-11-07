from django.urls import path
from .views import *

urlpatterns = [ 
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('rooms/', RoomList.as_view()),
    path('rooms/<int:pk>/', RoomDetail.as_view()),
    path('players/', PlayerList.as_view()),
    path('players/<int:pk>/', PlayerDetail.as_view()),
    path('ranks/', RankList.as_view()),
    path('ranks/<int:pk>/', RankDetail.as_view()),
    path('extends/', ExtendUserList.as_view()),
    path('extends/<int:pk>/', ExtendUserDetail.as_view()),
]