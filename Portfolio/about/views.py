from django.shortcuts import render
from .models import aboutData,ourTeam

# Create your views here.
def about(request):
    ab_Data =aboutData.objects.all()[0]
    context={
        'about': ab_Data
    }
    return render(request,'About/about.html',context)
def team(request):
    team_Data = ourTeam.objects.all()
    context  = {
        'teamMember': team_Data
    }
    return render(request,'About/ourteam.html',context)

