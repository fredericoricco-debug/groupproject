from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import loader

from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User


@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            newUser = User.objects.create_user(username, email, password1)

            newUser.save()

            messages.success(request, "Account successfully created.")
            return redirect('signin')

    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "home.html", {'username': username})
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.info(request, "You have succesfully logged out.")
    return redirect("signin")
