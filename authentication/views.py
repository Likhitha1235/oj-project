from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home_view(request):
    if request.method == "POST":
        usertype_requested = request.POST.get("usertype")
        username_requested = request.POST.get("username")
        password_requested = request.POST.get("password")

        if username_requested == "" or password_requested == "":
            messages.add_message(request,messages.INFO, "Please enter all the credentials")

        if not User.objects.filter(username = username_requested).exists():
            messages.add_message(request,messages.INFO, "No such user exists")
            messages.add_message(request,messages.INFO, "please register")
            return render(request,"home.html", {})

        
        user = authenticate(request, username = username_requested, password = password_requested)
        return redirect("problems/")

        if user is not None:
            login(request,user)
            return redirect("register/temp/")
        else:
            return render(request, "home.html", {})

    return render(request, "home.html", {})

def register_view(request):

    if request.method == "POST":
        username_requested = request.POST.get("username")
        password_requested = request.POST.get("password")

        any_user = User.objects.filter(username = username_requested)

        if any_user.exists():
            return render(request,"register.html", {})

        user = User.objects.create_user(username = username_requested)
        user.set_password(password_requested)
        user.save() 

        return redirect("temp/") 

    return render(request,"register.html",{})

def temp_view(request):
    return HttpResponse("<h1>This is view page </h1>")



