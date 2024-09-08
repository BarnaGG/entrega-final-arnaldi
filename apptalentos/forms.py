from django import forms

class StreamerForm(forms.Form):
    tag = forms.CharField(max_length=40)
    twitch = forms.URLField(max_length=80)
    youtube = forms.URLField(max_length=80)
    twitter = forms.URLField(max_length=80)
    instagram = forms.URLField(max_length=80)
    tiktok = forms.URLField(max_length=80)
    photo = forms.ImageField()
    
class HostCasterForm(forms.Form):
    tag = forms.CharField(max_length=40)
    twitch = forms.URLField(max_length=80)
    twitter = forms.URLField(max_length=80)
    instagram = forms.URLField(max_length=80)
    reel = forms.URLField(max_length=80)
    dossier = forms.URLField(max_length=80)
    photo = forms.ImageField()
    
class PlayerForm(forms.Form):
    tag = forms.CharField(max_length=40)
    twitch = forms.URLField(max_length=80)
    youtube = forms.URLField(max_length=80)
    twitter = forms.URLField(max_length=80)
    instagram = forms.URLField(max_length=80)
    game = forms.CharField(max_length=40)
    role = forms.CharField(max_length=40)
    former = forms.CharField(max_length=100)
    photo = forms.ImageField()
    
class InfluencerForm(forms.Form):
    tag = forms.CharField(max_length=40)
    twitch = forms.URLField(max_length=80)
    youtube = forms.URLField(max_length=80)
    twitter = forms.URLField(max_length=80)
    instagram = forms.URLField(max_length=80)
    tiktok = forms.URLField(max_length=80)
    photo = forms.ImageField()