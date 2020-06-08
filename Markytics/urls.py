from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('incident.urls', namespace="incident")),
    path('', include('person.urls', namespace="person")),
    path('admin/', admin.site.urls),
]
