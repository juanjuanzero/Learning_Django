from django.urls import path

from meetings.views import detail, allRooms

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('allRooms', allRooms, name='all_rooms')
]