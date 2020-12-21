from django.db import models

# Create your models here.

class MovieData(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    #api endpoints - user can ask for perticular gener of movie using it
    typ = models.CharField(max_length=200,default='action')
    image = models.ImageField(upload_to='Images/',default="images/None/Noimg.jpg")
