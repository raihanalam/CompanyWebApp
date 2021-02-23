from django.contrib import admin

# Register your models here.
from .models import aboutData,ourTeam

admin.site.register(aboutData)
admin.site.register(ourTeam)
