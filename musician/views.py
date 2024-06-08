from django.shortcuts import render,redirect
from . import forms
from . import models
from album.models import Album
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def musician(request):
    if request.method=='POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect(musician)
    else:
        musician_form = forms.MusicianForm()
        return render(request,'musician.html',{'form': musician_form})

@login_required
def edit_musician(request, id):
    mus = models.Musician.objects.get(pk=id) 
    musician_form = forms.MusicianForm(instance=mus)
    
    if request.method == 'POST': 
        musician_form = forms.MusicianForm(request.POST, instance=mus) 
        if musician_form.is_valid(): 
            musician_form.save()
            return redirect('homepage')
    
    return render(request, 'musician.html', {'form' : musician_form})
@login_required
def delete_all(request, id):
    mu = models.Musician.objects.get(pk=id) 
    mu.delete()
    return redirect('homepage')

