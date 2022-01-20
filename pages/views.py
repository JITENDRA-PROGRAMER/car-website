from django.shortcuts import render

# Create your views here.

# Home page function
def Home(request):
    return render(request,'pages/home.html')

def About(request):
    return render(request,'pages/about.html')

def Servecs(request):
    return render(request,'pages/servec.html')

def Contact(request):
    return render(request,'pages/contact.html')