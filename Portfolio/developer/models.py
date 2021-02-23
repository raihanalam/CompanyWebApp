from django.db import models

# Create your models here.
class geek(models.Model):
    geekedby = models.CharField(max_length=50,blank=False)
    topic = models.CharField(max_length=100,blank=False)
    geekpost = models.TextField(max_length=1000,blank=False)
    geektime = models.CharField(max_length=100,blank=False)
    def __str__(self):
        Title = self.geekedby + ', ' + self.topic
        return Title
