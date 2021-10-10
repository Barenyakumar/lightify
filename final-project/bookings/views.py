from django.shortcuts import render,redirect
from accounts.models import Blind,Helper
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def blind(request):
    if request.user.is_anonymous:
        return redirect('/')
    blinds=Blind.objects.all()
    return render(request,'blindpage.html',{'blinds':blinds})

def helper(request):
    if request.user.is_anonymous:
        return redirect('/')
    helpers=Helper.objects.all()
    return render(request,'helperpage.html',{'helpers':helpers})

def profile(request,profileuser):
    if request.user.is_anonymous:
        return redirect('/')
    if request.user.username == profileuser:
        profiledata=User.objects.get(username=profileuser)
        if Blind.objects.filter(username=profileuser).exists():
            avail=Blind.objects.get(username=profileuser).need_help
        else:
            avail=Helper.objects.get(username=profileuser).can_help
        context={
                "profiledata":profiledata,
                "avail":avail
        }
        return render(request,'profileown.html',context)

    profiledata=User.objects.get(username=profileuser)
    return render(request,'profile.html',{"profiledata":profiledata})

def togglebool(request):
    if request.user.is_anonymous:
        return redirect('/')
    username=request.user.username
    if Blind.objects.filter(username=username).exists():
        update_blind=Blind.objects.filter(username=username)[0]
        if update_blind.need_help==True:
            update_blind.need_help=False
        else:
            update_blind.need_help=True
        update_blind.save()
    else:
        update_helper=Helper.objects.filter(username=username)[0]
        if update_helper.can_help==True:
            update_helper.can_help=False
        else:
            update_helper.can_help=True
        update_helper.save()

    return redirect(f'/bookings/profile/{request.user.username}')

