from DispatchConsole.models import Incident, Location,IncidentNature,Message,Unit

class incidentdata:
    #must indent
    def get_incident_list():

        return Incident.objects.all()

    def get_incident(id):

        return Incident.objects.get(pk=id)
