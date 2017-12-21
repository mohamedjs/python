from django.http import HttpResponse
from .models import Album, Song
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template import loader

# Create your views here.
def index(request):
    all_album = Album.objects.all()
    context={
        'all_album':all_album,
    }
    return render(request,"music/index.html",context)
def detail(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('album doens,t exist')
    return render(request,'music/detail.html',{'album':album})
def artist(request):
    all_album = Album.objects.all()
    context = {
        'artists': all_album,
    }
    return render(request, "music/artist.html", context)