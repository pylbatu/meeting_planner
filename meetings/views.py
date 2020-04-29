from .models import Meeting, Room

from django.shortcuts import render, get_object_or_404

# Create your views here.


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {
        'meeting': meeting
    })


def rooms(request):
    rooms = Room.objects.all()
    return render(
        request,
        'rooms/list.html', {
            'rooms': rooms
        }
    )

def roomDetail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, 'rooms/detail.html', {
        'room': room
    })
