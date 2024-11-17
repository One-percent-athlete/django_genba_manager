from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import calendar
from django.utils.safestring import mark_safe
from django.contrib import messages
from .forms import RegisterForm
import datetime
x = datetime.datetime.now()

@login_required(login_url='/login/')
def dashboard(request, year, month, day):
    if request.user.is_authenticated:
        context = {
            "year": year,
            "month": month,
            "day": day,
        }
        return render(request, "dashboard.html", context=context)
    else:
        return redirect("login")
    

@login_required(login_url='/login/')
def report(request):    
        return render(request, "report.html")

    
@login_required(login_url='/login/')
def home(request):
    year = int(x.year)
    month = int(x.month)
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    cal = cal.replace('<td ', '<td width="150" height="150" hover')
    cal = mark_safe(cal)
    if request.user.is_authenticated:
         context = {
            "year": year,
            "month": month,
            "cal": cal,
        }
         return render(request, "home.html", context=context)
    else:
        return redirect('login')

    


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

@login_required(login_url='/login/')
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
            return redirect("login")
     else:
        form = RegisterForm()

     return render(request, "authenticate/register.html", {"form": form})
    
        