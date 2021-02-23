from django.db import models

# Create your models here.
class aboutData(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.CharField(max_length=600,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)
    def __str__(self):
        return self.title
class ourTeam(models.Model):
    name = models.CharField(max_length=50,blank=False)
    designation =models.CharField(max_length=100,blank=False)
    github = models.CharField(max_length=200,blank=False)
    linkedin = models.CharField(max_length=200,blank=False)
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about/OurTeam',blank=False)
    def __str__(self):
        return self.name