from django.shortcuts import render
from musician.models import Musician
from album.models import Album
# Create your views here.
def home(request):
    data = Musician.objects.all()
    data_al = Album.objects.all()
    return render(request,'index.html',{'data':data,'data_al':data_al})