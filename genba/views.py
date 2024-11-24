from cProfile import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import calendar
import datetime
x = datetime.datetime.now()

from .forms import RegisterForm, SignUpForm, UpdateUserForm, UserProfileForm

def update_user(request, user_id):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=user_id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Your Profile Has Been Updated Successfully.")
            return redirect("update_user", user_id)
        return render(request, "update_user.html", {"user_form": user_form})
    else:
        messages.success(request, "You Must Login First!")
        return redirect("home")
    
def update_profile(request, user_id):
    if request.user.is_authenticated:

        current_user = Profile.objects.get(user__id=user_id)
        form = UserProfileForm(request.POST or None, instance=current_user)
        if form.is_valid():

            form.save()
            messages.success(request, "Your Profile Has Been Updated Successfully.")
            return redirect("update_user", user_id)
        return render(request, "update_profile.html", {"form": form})
    else:
        messages.success(request, "You Must Login First!")
        return redirect("home")


def add_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Welcome To Our Online Shop. Please Fill Out Your Profile."))
            return redirect("update_profile", user.pk)
        else:
            messages.success(request, ("Whoops, There Was A Problem Registering, Please Try Agian.."))
            return redirect("login_user")
    else:
        return render(request, "add_user.html", {
            "form": form
        })

@login_required(login_url='/login_user/')
def home(request):
        return render(request, "home.html")

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
            return redirect("login_user")
    else:
        return render(request, "authenticate/login.html", {})   

@login_required(login_url='/login_user/')
def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out"))
    return redirect("login_user")

# def add_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password1"]
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("Registration Successful!!"))
                return redirect("login_user")
        else:
            form = RegisterForm()

        return render(request, "add_user.html", {"form": form})
    else:
        return redirect("login_user")
    

@login_required(login_url='/login_user/')
def user_list(request):    
        return render(request, "user_list.html")

@login_required(login_url='/login_user/')
def schedule(request):
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
         return render(request, "schedule.html", context=context)
    else:
        return redirect('login_user')

@login_required(login_url='/login/')
def schedule_details(request):
    return render(request, "schedule_details.html")

@login_required
def add_genba(request):
     if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!!"))
            return redirect("login_user")
     else:
        form = RegisterForm()

     return render(request, "add_genba.html", {"form": form})
    
@login_required(login_url='/login_user/')
def genba_list(request):    
        return render(request, "genba_list.html")

@login_required(login_url='/login_user/')
def genba_details(request):    
        return render(request, "genba_details.html")

@login_required(login_url='/login_user/')
def add_report(request):    
        return render(request, "add_report.html")

@login_required(login_url='/login_user/')
def report_list(request):    
        return render(request, "report_list.html")

@login_required(login_url='/login_user/')
def report_details(request):    
        return render(request, "report_details.html")


    