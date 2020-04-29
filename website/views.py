
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting
# Create your views here.


def welcome(request):
    return render(request, 'website/welcome.html', {
        'welcome_message': 'You are super!',
        'secret_message' : 'You are loved!',
        'meetings': Meeting.objects.all()
    })


def date(request):
    return HttpResponse('This request is made at ' + str(datetime.now()))


def about(request):
    return HttpResponse('<h1>About</h1> Pyl is Pyl!')