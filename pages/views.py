import imghdr
from django.shortcuts import render

from pages.models import Team
from .models import *
# Create your views here.

# Home page function
def Home(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'pages/home.html',data)



def About(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'pages/about.html',data)

def Servecs(request):
    return render(request,'pages/servec.html')

def Contact(request):
    return render(request,'pages/contact.html')