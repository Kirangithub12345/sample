from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.template import loader
#from pytube import YouTube 
#import re
#import math 
#import os 
#import requests
#from tqdm import tqdm

def home (request):
    #url = "https://youtu.be/RGo84RthjPY"
    
    
    return HttpResponse("hello kiran")
    
def house(request):
   # url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
#    req = requests.get(url)
#bs = BeautifulSoup(url)
#    r = re.findall("<title>.*</title>",str(req.text))
#    print(r)
    return HttpResponse("hello kiran")
    

