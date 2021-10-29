from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse

from meetings.models import Meeting


# Create your views here.
def welcome(request):
    if request.user.is_authenticated:
        mtgs = Meeting.objects.all()
        return render(request, "website/welcome.html", {"meetings": mtgs})
    else:
        return redirect("website/signin")

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, 'website/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'website/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'website/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'website/signup.html', {'form': form})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now().date()))


def about(request):
    return HttpResponse("Hello, world. I am Juan")
