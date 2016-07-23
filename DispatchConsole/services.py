from DispatchConsole.models import Incident, Location,IncidentNature,Message,Unit

def get_incident_list():

    return Incident.objects.all()
