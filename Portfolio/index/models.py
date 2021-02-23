from django.db import models

class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=600, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)
    def __str__(self):
        return self.title