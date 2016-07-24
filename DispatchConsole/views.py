from django.shortcuts import render
from DispatchConsole.services import incidentdata

# Create your views here.
from django.http import HttpResponse
#this index loads a example template with snippets {ryan}
def index(request):
    all_incidents = incidentdata.get_incident_list()

    return render(request,'main/current.html', {"incidents": all_incidents})

def show(request,iid):
    one_incident = incidentdata.get_incident(iid)

    return render(request,'main/incident-info.html', {"one_incident": one_incident})
