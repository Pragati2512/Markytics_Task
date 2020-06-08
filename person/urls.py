from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('', views.home , name='home'),
    path("login/", views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path("logout/", views.logout_request, name='logout'),

]
