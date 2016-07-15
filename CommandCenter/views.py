from django.shortcuts import render

# Create your views here.

#for inital routing testing only
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the command center module for the web911 application.")