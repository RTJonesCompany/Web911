from django.shortcuts import render
from DispatchConsole.services import get_incident_list

# Create your views here.
from django.http import HttpResponse
#this index loads a example template with snippets {ryan}
def index(request):
    all_incidents = get_incident_list()
    return render(request,'main/current.html', {"incidents": all_incidents})
