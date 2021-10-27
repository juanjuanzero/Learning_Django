from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Meeting, Room

# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request,"meetings/detail.html", {"meeting": meeting})

def delete(request, id):
    meeting = Meeting.objects.get(pk=id)
    if meeting:
        meeting.delete()
    return redirect("home")

def allRooms(request):
    rms = Room.objects.all()
    return render(request, "meetings/allRooms.html", {"rooms": rms})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})