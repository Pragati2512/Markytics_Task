from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import datetime

class severity(Enum):
    Mild = "Mild"
    Moderate = "Moderate"
    Severe = "Severe"
    Fatal = "Fatal"

class location(Enum):
    CorpHead = "Corporate Headoffice"
    OPD = "Operations Department"
    WS = "Work Station"
    MD = "Marketing Division"

class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
