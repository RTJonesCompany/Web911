from django.shortcuts import render

# Create your views here.

#for inital routing testing only
from django.http import HttpResponse


def index(request):
     return render(request,'main/example.html')
