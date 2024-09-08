from django.contrib import admin
from .models import Streamer, HostCaster, Player, Influencer

# Register your models here.

admin.site.register(Streamer)
admin.site.register(HostCaster)
admin.site.register(Player)
admin.site.register(Influencer)
