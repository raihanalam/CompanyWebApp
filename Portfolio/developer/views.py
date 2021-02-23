from django.shortcuts import render
from .models import geek
import datetime

# Create your views here.
def devhome(request):
    if request.method == 'POST':
        geekTopic = request.POST['topic']
        geekedBy = None
        if request.user.is_authenticated:
            geekedBy = request.user.username
        geekPost = request.POST['geekpost']
        formTime = datetime.datetime.now()
        geekTime = formTime.strftime("%H:%M:%S  %d-%m-%Y")
        geekData = geek(topic=geekTopic,geekedby=geekedBy,geekpost=geekPost,geektime=geekTime)
        geekData.save()
    geekData = geek.objects.all()
    context ={
        'geekdata': geekData
    }
    return render(request, 'Developer/home.html',context)

def profile(request):
    return render(request,'Developer/profile.html')
