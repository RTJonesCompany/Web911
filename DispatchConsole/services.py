from DispatchConsole.models import Incident, Location,IncidentNature,Message,Unit
from django.shortcuts import get_object_or_404

class incidentdata:
    #must indent
    def get_incident_list():

        return Incident.objects.all()

    def get_incident(id):

        return get_object_or_404(Incident, pk=id)
