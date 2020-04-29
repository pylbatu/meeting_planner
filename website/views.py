
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def welcome(request):
    return HttpResponse('Welcome to your website Pyl!')


def date(request):
    return HttpResponse('This request is made at ' + str(datetime.now()))
