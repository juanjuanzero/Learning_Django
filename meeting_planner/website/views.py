from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,"website/welcome.html", {"message": "hello world, this is a message from the view function!"})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now().date()))

def about(request):
    return HttpResponse("Hello, world. I am Juan")