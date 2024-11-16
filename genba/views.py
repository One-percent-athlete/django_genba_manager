from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def home(request, year, month):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("login")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("Username Or Password Was Not Correct, Please Try Again."))
            return redirect("login")
    else:
        return render(request, "authenticate/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out"))
    return redirect("home")

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
    
        