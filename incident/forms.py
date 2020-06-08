from .models import incident
from django import forms

class IncidentForm(forms.ModelForm):
    class Meta:
        model = incident
        fields = ("location1", "location2", "description" , "severity" , "cause" , "date", "time", "actions" ,
                  "type_env" , "type_inju" , "type_property" , "type_vehicle" )
