from django.shortcuts import render
from DispatchConsole.services import get_incident_list

# Create your views here.
from django.http import HttpResponse
#this index loads a example template with snippets {ryan}
def index(request):
    return render(request,'main/current.html', get_incident_list)
