from django import forms
import json
from .models import Incident, Location

#def getStatesList(key_field=None):
#    with open(STATICFILES_DIR+'states.json') as f:
#        json_data = json.load(f)
#        choices_list = []
#        if key_field and key_field in json_data:
#            fields = json_data[key_field]
#            for field in fields:
#                choices_list.append((field, field))
#    return tuple(choices_list)

#STATES_LIST = getStatesList()
class CreateLocationForm(forms.ModelForm):
    class Meta:
            model = Location
            fields = [
                "address",
                "addressInfo",
                "city",
                "state",
                "county",
                "zipcode",
                "lat",
                "lng",
            ]
