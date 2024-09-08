from django.shortcuts import render, redirect
from .models import Streamer, HostCaster, Player, Influencer
from .forms import StreamerForm, HostCasterForm, PlayerForm, InfluencerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

# Views de renderizado directo
def inicio(req):
    return render(req, 'apptalentos/inicio.html')

@login_required    
def success_page(request):
    return render(request, 'apptalentos/success_page.html')

def conoceme(req):
    return render(req, 'apptalentos/conoceme.html')

# View de desplegable de ingreso de creator, redirigiendo al form correcto segun seleccion del usuario
@login_required
def add_creator(request):
    form = None
    selected_creator_type = request.POST.get('creator_type', None)
    
    if request.method == 'POST':
        
        if selected_creator_type == 'streamer':
            form = StreamerForm(request.POST, request.FILES)
            if form.is_valid():
                streamer = Streamer(
                    tag=form.cleaned_data['tag'],
                    twitch=form.cleaned_data['twitch'],
                    youtube=form.cleaned_data['youtube'],
                    twitter=form.cleaned_data['twitter'],
                    instagram=form.cleaned_data['instagram'],
                    tiktok=form.cleaned_data['tiktok'],
                    photo=form.cleaned_data['photo']
                )
                streamer.save()  
                return redirect('success_page')
            
        elif selected_creator_type == 'hostcaster':
            form = HostCasterForm(request.POST, request.FILES)
            if form.is_valid():
                hostcaster = HostCaster(
                    tag=form.cleaned_data['tag'],
                    twitch=form.cleaned_data['twitch'],
                    twitter=form.cleaned_data['twitter'],
                    instagram=form.cleaned_data['instagram'],
                    reel=form.cleaned_data['reel'],
                    dossier=form.cleaned_data['dossier'],
                    photo=form.cleaned_data['photo']
                )
                hostcaster.save()  
                return redirect('success_page')
            
        elif selected_creator_type == 'player':
            form = PlayerForm(request.POST, request.FILES)
            if form.is_valid():
                player = Player(
                    tag=form.cleaned_data['tag'],
                    twitch=form.cleaned_data['twitch'],
                    youtube=form.cleaned_data['youtube'],
                    twitter=form.cleaned_data['twitter'],
                    instagram=form.cleaned_data['instagram'],
                    game=form.cleaned_data['game'],
                    role=form.cleaned_data['role'],
                    former=form.cleaned_data['former'],
                    photo=form.cleaned_data['photo']
                )
                player.save()  
                return redirect('success_page')
            
        elif selected_creator_type == 'influencer':
            form = InfluencerForm(request.POST, request.FILES)
            if form.is_valid():
                influencer = Influencer(
                    tag=form.cleaned_data['tag'],
                    twitch=form.cleaned_data['twitch'],
                    youtube=form.cleaned_data['youtube'],
                    twitter=form.cleaned_data['twitter'],
                    instagram=form.cleaned_data['instagram'],
                    tiktok=form.cleaned_data['tiktok'],
                    photo=form.cleaned_data['photo']
                )
                influencer.save()  
                return redirect('success_page')

        if form and form.is_valid():
            form.save()
            return redirect('success_page')

    return render(request, 'apptalentos/add_creator.html', {
        'form': form,
        'selected_creator_type': selected_creator_type,
    })


# Views basadas en Clases - Streamers
class StreamersListView(LoginRequiredMixin, ListView):
    model = Streamer
    template_name = "apptalentos/VistasClases/streamers_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class StreamersDetailView(LoginRequiredMixin, DetailView):
    model = Streamer
    template_name = "apptalentos/VistasClases/streamers_detail.html"
    
class StreamersUpdateView(LoginRequiredMixin, UpdateView):
    model = Streamer
    success_url = reverse_lazy("StreamerList")
    fields = ["tag", "twitch", "youtube", "twitter", "instagram", "tiktok", "photo"]
    template_name = "apptalentos/VistasClases/streamers_update.html"

class StreamersDeleteView(LoginRequiredMixin, DeleteView):
    model = Streamer
    success_url = reverse_lazy("StreamerList")
    template_name = 'apptalentos/VistasClases/streamers_confirm_delete.html'

# Views basadas en Clases - HostCasters
class HostCastersListView(LoginRequiredMixin, ListView):
    model = HostCaster
    template_name = "apptalentos/VistasClases/hostcasters_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class HostCastersDetailView(LoginRequiredMixin, DetailView):
    model = HostCaster
    template_name = "apptalentos/VistasClases/hostcasters_detail.html"
    
class HostCastersUpdateView(LoginRequiredMixin, UpdateView):
    model = HostCaster
    success_url = reverse_lazy("HostcasterList")
    fields = ["tag", "twitch", "twitter", "instagram", "reel", "dossier", "photo"]
    template_name = "apptalentos/VistasClases/hostcasters_update.html"

class HostCastersDeleteView(LoginRequiredMixin, DeleteView):
    model = HostCaster
    success_url = reverse_lazy("HostcasterList")
    template_name = 'apptalentos/VistasClases/hostcasters_confirm_delete.html'

# Views basadas en Clases - Players
class PlayersListView(LoginRequiredMixin, ListView):
    model = Player
    template_name = "apptalentos/VistasClases/players_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PlayersDetailView(LoginRequiredMixin, DetailView):
    model = Player
    template_name = "apptalentos/VistasClases/players_detail.html"
    
class PlayersUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    success_url = reverse_lazy("PlayerList")
    fields = ["tag", "twitch", "youtube", "twitter", "instagram", "game", "role", "former", "photo"]
    template_name = "apptalentos/VistasClases/players_update.html"

class PlayersDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = reverse_lazy("PlayerList")
    template_name = 'apptalentos/VistasClases/players_confirm_delete.html'

# Views basadas en Clases - Influencers
class InfluencersListView(LoginRequiredMixin, ListView):
    model = Influencer
    template_name = "apptalentos/VistasClases/influencers_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class InfluencersDetailView(LoginRequiredMixin, DetailView):
    model = Influencer
    template_name = "apptalentos/VistasClases/influencers_detail.html"
    
class InfluencersUpdateView(LoginRequiredMixin, UpdateView):
    model = Influencer
    success_url = reverse_lazy("InfluencerList")
    fields = ["tag", "twitch", "youtube", "twitter", "instagram", "tiktok", "photo"]
    template_name = "apptalentos/VistasClases/influencers_update.html"

class InfluencersDeleteView(LoginRequiredMixin, DeleteView):
    model = Influencer
    success_url = reverse_lazy("InfluencerList")
    template_name = 'apptalentos/VistasClases/influencers_confirm_delete.html'




