from django.db import models

# Create your models here.
class Musician(models.Model):
    first_Name = models.CharField(max_length=15)
    last_Name = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_Name
    

    