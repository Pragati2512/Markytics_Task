from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import person, User


def home(request):
    return render(request, 'index.html')


def register(request):
    form1 = UserForm()
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        if form1.is_valid() :
            uss = form1.save()
            prsn= person(user=uss)
            prsn.save()
            login(request, uss)
            return redirect("person:home")
        message = 'ERROR !! Could not register. Please try again. '
        print("Error")
        context = {'message': message , 'form1': form1}
        return render(request,  'registration/registration_form2.html', context)
    return render(request, 'registration/registration_form2.html', {'form1': form1 })



def login_request(request):
    message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = "Success: You are now logged in."
                  #as {{request.user.username}}."
                return render(request, 'index.html',{"message": message,})
            else:
                message = "Error: Invalid username or password."
        else:
            message = "Error: Invalid username or password."
    form = AuthenticationForm()
    context = {"form": form,
               "message": message, }
    return render(  request = request, template_name = "registration/login.html", context=context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("person:home")


