import imghdr
from django.shortcuts import render

from pages.models import Team
from .models import *
from cars.models import Car
# Create your views here.

# Home page function
def Home(request):
    teams = Team.objects.all()
    feature_car = Car.objects.order_by('-created_date').filter(is_feature=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams':teams,
        'feature_car':feature_car,
        'all_cars':all_cars,
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