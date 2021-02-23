from django.contrib import admin
from .models import contactInfo,contactForm

# Register your models here.
admin.site.register(contactInfo),
admin.site.register(contactForm)