from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Hello there! Welcome to the Meeting Planner")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now().date()))

def about(request):
    return HttpResponse("Hello, world. I am Juan")