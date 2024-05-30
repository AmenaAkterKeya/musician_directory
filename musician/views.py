from django.shortcuts import render,redirect
from . import forms
from . import models
from album.models import Album
# Create your views here.
def musician(request):
    if request.method=='POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect(musician)
    else:
        musician_form = forms.MusicianForm()
        return render(request,'musician.html',{'form': musician_form})


def edit_musician(request, id):
    mus = models.Musician.objects.get(pk=id) 
    musician_form = forms.MusicianForm(instance=mus)
    
    if request.method == 'POST': 
        musician_form = forms.MusicianForm(request.POST, instance=mus) 
        if musician_form.is_valid(): 
            musician_form.save()
            return redirect('homepage')
    
    return render(request, 'musician.html', {'form' : musician_form})

def delete_all(request, id):
    mu = models.Musician.objects.get(pk=id) 
    mu.delete()
    return redirect('homepage')


# def delete_all(request, musician_id, album_id):
#     mu = models.Musician.objects.get(pk=musician_id) 
#     al = models.Album.objects.get(Album, pk=album_id)
#     mu.delete()
#     al.delete()
#     return redirect('homepage')