from django.db import models
from musician.models import Musician
# Create your models here.

Rating_choice= [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]
class Album(models.Model):
 
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_Name=models.CharField(max_length=15)
    release_date = models.DateField()
    rating= models.IntegerField(choices=Rating_choice)
    


    
    def __str__(self):
        return self.album_Name
    
    