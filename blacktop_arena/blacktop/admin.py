from django.contrib import admin
from .models import User, Player, Game


admin.site.register(User)
admin.site.register(Game)
admin.site.register(Player)