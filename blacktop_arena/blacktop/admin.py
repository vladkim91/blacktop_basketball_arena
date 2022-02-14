from django.contrib import admin
from .models import Player, Game, Team, Squad
# from django.contrib.auth.admin import UserAdmin

# admin.site.register(User, UserAdmin)

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Squad)
