from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("login")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")