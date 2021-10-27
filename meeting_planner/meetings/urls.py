from django.urls import path

from meetings.views import detail, allRooms, new, delete

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('allRooms', allRooms, name='all_rooms'),
    path('new', new, name='new'),
    path('delete/<int:id>', delete, name='delete')
]