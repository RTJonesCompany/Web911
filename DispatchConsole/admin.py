from django.contrib import admin

# Register your models here.
from DispatchConsole.models import Incident,Message,IncidentNature,Location,Unit,UnitType

admin.site.register(Incident)
#admin.site.register(IncidentMessage)
admin.site.register(Message)
admin.site.register(IncidentNature)
admin.site.register(Location)
admin.site.register(Unit)
admin.site.register(UnitType)
