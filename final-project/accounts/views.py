from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Helper,Blind

# Create your views here.
def home(request):
    helpers=Helper.objects.all()
    blinds=Blind.objects.all()
    context={
        "blinds":blinds,
        "helpers": helpers
    }
    if request.user.is_anonymous:
        return render(request,"newuserhome.html",context)
    return render(request,"loggedinuser.html",context)


def loginUser(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            messages.warning(request,"Wrong authentication details")
            return render(request,"newuserhome.html")
            # No backend authenticated the credentials
    return redirect("/")


def logoutuser(request):
    logout(request)
    return redirect('/')


def signupuser(request,profile):
    if request.method == "POST":
        username = request.POST.get("username")
        email= request.POST.get("email")
        password = request.POST.get("password")
        repeatpassword= request.POST.get("repeatpassword")
        if(password!=repeatpassword):
            messages.warning(request,"Both your entries for password doesn't match")
            return render(request,"newuserhome.html")

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already in use')
            return render(request, 'newuserhome.html')
        else:
            user = User.objects.create_user(
                username=username, password=password,email=email)
            if profile=="helper":
                new_helper=Helper(username=username)
                new_helper.save()
            elif profile=="blind":
                new_blind=Blind(username=username)
                new_blind.save()
            return redirect('/')
    return redirect('/')
