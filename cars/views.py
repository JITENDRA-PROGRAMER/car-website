from django.shortcuts import render

# Create your views here.

def Car(request):
    return render(request,'cars/cars.html')