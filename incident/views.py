from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import IncidentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import incident
from person.models import person


def create_incident(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            inci = form.save(False)
            inci.reported_by = person.objects.get(user=request.user)
            form.save(True)
            return redirect('person:home')
        else:
            return HttpResponse("Wrong Response.")
    else:
        form = IncidentForm()
        context = {"form": form, }
        return render(request, 'incident/incident_form.html', context)
