from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(ExtendUser)
admin.site.register(Room)
admin.site.register(PlayerGame)
admin.site.register(Rank)