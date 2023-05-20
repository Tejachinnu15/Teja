from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srujana(request):
    return HttpResponse('<marquee><h1>srujana Tinnavara</marquee></h1>')
def meghana(request):
    return HttpResponse('<marquee><b>my name is meghana sir</marquee></h1>')
