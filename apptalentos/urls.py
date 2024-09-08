from django.urls import path
from apptalentos import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('add_creator/', views.add_creator, name='add_creator'),
    path('success_page/', views.success_page, name='success_page'),
    path('conoceme/', views.conoceme, name='conoceme'),   
]

# Streamers
urlpatterns += [
    path('streamerslist/', views.StreamersListView.as_view(), name="StreamerList"),
    path('streamerdetail/<int:pk>/', views.StreamersDetailView.as_view(), name="StreamerDetail"),
    path('streamerupdate/<int:pk>/', views.StreamersUpdateView.as_view(), name="StreamerUpdate"),
    path('streamerdelete/<int:pk>/', views.StreamersDeleteView.as_view(), name="StreamerDelete"),
]

# HostCasters
urlpatterns += [
    path('hostcasterslist/', views.HostCastersListView.as_view(), name="HostcasterList"),
    path('hostcasterdetail/<int:pk>/', views.HostCastersDetailView.as_view(), name="HostcasterDetail"),
    path('hostcasterupdate/<int:pk>/', views.HostCastersUpdateView.as_view(), name="HostcasterUpdate"),
    path('hostcasterdelete/<int:pk>/', views.HostCastersDeleteView.as_view(), name="HostcasterDelete"),
]

# Players
urlpatterns += [
    path('playerslist/', views.PlayersListView.as_view(), name="PlayerList"),
    path('playerdetail/<int:pk>/', views.PlayersDetailView.as_view(), name="PlayerDetail"),
    path('playerupdate/<int:pk>/', views.PlayersUpdateView.as_view(), name="PlayerUpdate"),
    path('playerdelete/<int:pk>/', views.PlayersDeleteView.as_view(), name="PlayerDelete"),
]

# Influencers
urlpatterns += [
    path('influencerslist/', views.InfluencersListView.as_view(), name="InfluencerList"),
    path('influencerdetail/<int:pk>/', views.InfluencersDetailView.as_view(), name="InfluencerDetail"),
    path('influencerupdate/<int:pk>/', views.InfluencersUpdateView.as_view(), name="InfluencerUpdate"),
    path('influencerdelete/<int:pk>/', views.InfluencersDeleteView.as_view(), name="InfluencerDelete"),
]