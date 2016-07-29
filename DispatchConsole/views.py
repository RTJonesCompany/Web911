#from googlemaps import client
from django.shortcuts import render, get_object_or_404
import json
from DispatchConsole.services import incidentdata

# Create your views here.
from .forms import CreateLocationForm

from django.http import HttpResponse
#this index loads a example template with snippets {ryan}
def index(request):
    all_incidents = incidentdata.get_incident_list()

    return render(request,'main/current.html', {"incidents": all_incidents})

def show(request,iid):
    one_incident = incidentdata.get_incident(iid)

    return render(request,'main/incident-info.html', {"one_incident": one_incident})

def location_create(request):
    #api ="AIzaSyDNpsBSt_WLcBArOssZJ-iBaZDJzgrTMks"


    form = CreateLocationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    #if request.method == "POST":
        #gmaps = googlemaps.Client(key='AIzaSyDNpsBSt_WLcBArOssZJ-iBaZDJzgrTMks')
    #    print (request.POST.get("address"))
    #    address = request.POST.get("address")
    #    print (request.POST.get("addressInfo"))
    #    addressInfo = request.POST.get("addressInfo")
    #    print (request.POST.get("city"))
    #    city = request.POST.get("city")
    #    print (request.POST.get("state"))
    #    state =  request.POST.get("state")
    #    print (request.POST.get("county"))
    #    county = request.POST.get("county")
    #    print (request.POST.get("zipcode"))
    #    zipcode = request.POST.get("zipcode")
    #    addrstring = address+','+city+','+state
        #print (addrstring)
        #latlng = gmaps.geocode(addrstring)
        #r = request.get("https://maps.googleapis.com/maps/api/geocode/json?"+addrstring="&key="+api)
        #r = request.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDNpsBSt_WLcBArOssZJ-iBaZDJzgrTMks')
        #json = r.json()

        #print(json)

    #data to pass
    context =   {
    "form" : form,

    }
    return render(request,"main/create_location.html", context)

def update_location(request):

    return(request,"main/update_location.html")
