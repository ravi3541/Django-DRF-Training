from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

    


class Song(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='songs')

    def __str__(self):
        return str(self.year) + " " +self.title