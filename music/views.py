# Create your views here.
from django.shortcuts import render

from music.models import Artists

def index(request):
  artists = Artists.objects.all().order_by('name')
  context = {'artists': artists}
  return render(request, 'music/index.html', context)
