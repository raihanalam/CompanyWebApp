from django.db import models

# Create your models here.
class contactInfo(models.Model):
    phone = models.CharField(max_length=30,blank=False)
    email = models.CharField(max_length=50,blank=False)
    locations = models.CharField(max_length=100,blank=False)

class contactForm(models.Model):
    fullName = models.CharField(max_length=30,blank=False)
    email = models.CharField(max_length=50,blank=False)
    subject = models.CharField(max_length=300,blank=False)
    message = models.TextField(max_length=800,blank=False)
    def __str__(self):
        return self.subject
