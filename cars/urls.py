from django.urls import path

from pages import views

from .import views
urlpatterns = [
   path('',views.Car,name="cars"),
]
