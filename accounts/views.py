from django.contrib import messages
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from travello.models import Destination

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print("user Created")
                return redirect('login')
        else:
            messages.info(request,'Passwords not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def information(request):
    name = request.POST["name"]
    return render(request,'information.html',{'name':name})
