from django.shortcuts import render
from .models import slider
from about.models import aboutData

def home(request):
    aboutInfo= aboutData.objects.all()[0]
    sliderData = slider.objects.all()
    context ={
        'about': aboutInfo,
        'slider': sliderData
    }
    return render(request, 'index.html',context)
