# Create your views here.
from django.shortcuts import render
from music.models import Artists, Albums, Tracks
from django.core import serializers
from django.http import HttpResponse


def index(request):
    artists = Artists.objects.all().order_by('name')
    context = {'artists': artists}
    return render(request, 'music/index.html', context)


def tracks(request, artist=None):
    tracks = Tracks.objects.filter(album__artist=artist)
    data = serializers.serialize('json', tracks)
    return HttpResponse(data, mimetype='application/json')
