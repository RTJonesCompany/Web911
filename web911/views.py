from django.shortcuts import render
from DispatchConsole.services import dataservices

# Create your views here.
from django.http import HttpResponse
#this index loads a example template with snippets {ryan}
def index(request):
    all_incidents = get_incident_list()
    one_incident = get_incident_byid(1)
    return render(request,'main/current.html', {"incidents": all_incidents, "one_incident": one_incident})
