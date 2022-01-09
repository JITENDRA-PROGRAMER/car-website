from django.shortcuts import render

# Create your views here.

# Home page function
def Home(request):
    return render(request,'pages/home.html')