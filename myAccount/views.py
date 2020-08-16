from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django_email_verification import sendConfirm
# Create your views here.

def LogOut(request):
    auth.logout(request)
    return redirect("/")

def LogIn(request):
    if request.method=="POST":
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        user = auth.authenticate(username=Email,password=Password)
        if user is not None:
            auth.login(request,user)
            if request.GET.get('next',None):
                return HttpResponseRedirect(request.GET["next"])
            return redirect("/")
        else:
            messages.info(request,"Account Not Exists")
            redirect("LogIn.html")
    return render(request,"LogIn.html")

def SignUp(request):
    if request.method=="POST":
        first_name = request.POST.get("FullName")
        name = first_name.split(" ")
        last_name = name[-1]
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        Conf_Password = request.POST.get("Conf_Password")
        if (Password == Conf_Password):
            if (User.objects.filter(username=Email).exists()) or (User.objects.filter(email=Email).exists()):
                messages.info(request,"Username or Email Already taken")
                redirect("signUp.html")
            else:
                user = User.objects.create_user(username=Email, email=Email, password=Password, first_name = first_name, last_name=last_name)
                user.save()
                sendConfirm(user)
                users = auth.authenticate(username=Email,password=Password)
                auth.login(request,users)
                return redirect("/")
        else:
            messages.info(request,"Password not match")
            redirect("signUp.html")
    return render(request,"signUp.html")
    