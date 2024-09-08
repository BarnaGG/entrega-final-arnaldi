from django.db import models

# Create your models here.

class Streamer(models.Model):
    tag = models.CharField(max_length=40)
    twitch = models.URLField(max_length=80)
    youtube = models.URLField(max_length=80)
    twitter = models.URLField(max_length=80)
    instagram = models.URLField(max_length=80)
    tiktok = models.URLField(max_length=80)
    photo = models.ImageField(upload_to='streamers_photos/')

class HostCaster(models.Model):
    tag = models.CharField(max_length=40)
    twitch = models.URLField(max_length=80)
    twitter = models.URLField(max_length=80)
    instagram = models.URLField(max_length=80)
    reel = models.URLField(max_length=80)
    dossier = models.URLField(max_length=80)
    photo = models.ImageField(upload_to='HostCasters_photos/')

class Player(models.Model):
    tag = models.CharField(max_length=40)
    twitch = models.URLField(max_length=80)
    youtube = models.URLField(max_length=80)
    twitter = models.URLField(max_length=80)
    instagram = models.URLField(max_length=80)
    game = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    former = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='players_photos/')
    
class Influencer(models.Model):
    tag = models.CharField(max_length=40)
    twitch = models.URLField(max_length=80)
    youtube = models.URLField(max_length=80)
    twitter = models.URLField(max_length=80)
    instagram = models.URLField(max_length=80)
    tiktok = models.URLField(max_length=80)
    photo = models.ImageField(upload_to='influencers_photos/')