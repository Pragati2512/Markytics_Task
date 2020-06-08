from django.urls import path
from . import views

app_name = 'incident'

urlpatterns = [
    path("incident-form/", views.create_incident, name='create-inci'),

    ]
