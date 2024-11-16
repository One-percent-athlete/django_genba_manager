from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
import datetime
x = datetime.datetime.now()

def home(request, year, month, day):
    if request.user.is_authenticated:
        context = {
            "year": x.year,
            "month": x.month,
            "date":x.day
        }
        return render(request, "home.html", context=context)
    else:
        return redirect("login")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home", year=x.year, month=x.month, day=x.day)
        else:
            messages.success(request, ("Username Or Password Was Not Correct, Please Try Again."))
            return redirect("login")
    else:
        return render(request, "authenticate/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out"))
    return redirect("login")

def register_user(request):
     if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!!"))
            return redirect("home")
     else:
        form = RegisterForm()

     return render(request, "authenticate/register.html", {"form": form})
    
        