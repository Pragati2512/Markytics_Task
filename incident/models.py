from django.db import models
from person.models import person
from enum import Enum
import datetime

class severity(Enum):
    Mild = "Mild"
    Moderate = "Moderate"
    Severe = "Severe"
    Fatal = "Fatal"


class location(Enum):
    CH = "Corporate Headoffice"
    OPD = "Operations Department"
    WS = "Work Station"
    MD = "Marketing Division"


class incident(models.Model):
    location1 = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in location],
                                   default=location.CH)
    location2 = models.TextField(default="abcd")
    description = models.TextField(default="abcd")
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.time)
    severity = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in severity],
                                   default=severity.Mild)
    cause = models.TextField(default="abcd")
    actions  = models.TextField(default="abcd")
    type_env = models.BooleanField(default=False)
    type_inju = models.BooleanField(default=False)
    type_property = models.BooleanField(default=False)
    type_vehicle = models.BooleanField(default=False)
    reported_by = models.ForeignKey(person, on_delete=None)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.location2
