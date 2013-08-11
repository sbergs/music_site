# Create your views here.
from django.shortcuts import render

from music.models import Artists, Albums, Tracks


def index(request):
    artists = Artists.objects.all().order_by('name')
    context = {'artists': artists}
    return render(request, 'music/index.html', context)


def tracks(request, artist=None):
    tracks = Tracks.objects.filter(album__artist=artist)
    context = {'tracks': tracks}
    return render(request, 'music/index.html', context)
