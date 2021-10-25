from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

from meetings.models import Meeting

# Create your views here.
def welcome(request):
    mtgs = Meeting.objects.all()
    return render(request,"website/welcome.html", {"meetings": mtgs})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now().date()))

def about(request):
    return HttpResponse("Hello, world. I am Juan")