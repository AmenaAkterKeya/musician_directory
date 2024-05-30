
from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
    
    else:
        album_form = forms.AlbumForm()
    return render(request, 'album.html', {'form' : album_form})

def edit_album(request, id):
    alb = models.Album.objects.get(pk=id) 
    album_form = forms.AlbumForm(instance=alb)
    
    if request.method == 'POST': 
        album_form = forms.AlbumForm(request.POST, instance=alb) 
        if album_form.is_valid(): 
            album_form.save()
            return redirect('homepage')
    
    return render(request, 'album.html', {'form' : album_form})




