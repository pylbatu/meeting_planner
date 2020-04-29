from .models import Meeting

from django.shortcuts import render

# Create your views here.


def detail(request, id):
    meeting = Meeting.objects.get
    return render(request, 'meetings/detail.html', {
        'meeting': meeting
    })
