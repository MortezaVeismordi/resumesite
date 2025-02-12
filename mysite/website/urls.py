from django.contrib import admin
from django.urls import path
from website.views import *

app_name = "website"

urlpatterns = [
    path('' , index , name= 'home'),
    path('home' , index , name= 'home'),
    path('about' , about_me , name= 'about'),
    path('contact' , contact_me , name= 'contact'),
    path('resume' , my_resume , name= 'resume'),
    path('services' , my_services , name= 'services'),
    path('portfolio' , my_portfolio , name= 'portfolio'),
]
