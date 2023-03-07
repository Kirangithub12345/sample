from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'ytproject'
urlpatterns = [
    path('',views.home, name = 'home'),
    path('house',views.house,name = 'house'),
    
]