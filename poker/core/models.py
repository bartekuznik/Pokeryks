from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coin_numbers = models.PositiveIntegerField(default=True)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return self.user
    

class Room(models.Model):
    card_1 = models.TextField(max_length=20)
    card_2 = models.TextField(max_length=20)
    card_3 = models.TextField(max_length=20)
    card_4 = models.TextField(max_length=20)
    card_5 = models.TextField(max_length=20)
    max_player_num = models.PositiveIntegerField()
    current_player_num = models.PositiveBigIntegerField(default=0)
    coins = models.PositiveIntegerField()


class PlayerGame(models.Model):
    player = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    player_room = models.OneToOneField(Room, on_delete=models.DO_NOTHING)
    victory = models.DecimalField(max_digits=3, decimal_places=2)
    card_1 = models.TextField(max_length=20)
    card_2 = models.TextField(max_length=20)
    is_win = models.BooleanField(blank=True)

class Rank(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    win_number = models.PositiveIntegerField()
