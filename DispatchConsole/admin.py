from django.contrib import admin

# Register your models here.
from DispatchConsole.models import Incident,Message,IncidentMessage,IncidentNature,Location

admin.site.register(Incident)
admin.site.register(IncidentMessage)
admin.site.register(Message)
admin.site.register(IncidentNature)
admin.site.register(Location)
