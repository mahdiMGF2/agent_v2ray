from django.shortcuts import render,redirect
from .forms import Loginfrom,Registerfrom
from django.contrib.auth import login,authenticate
from .models import User
# Create your views here.

def Dashboard(request):
    if str(request.user) == "AnonymousUser":
        return redirect('/login')
    return render(request,'dashboard.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect('user_agent:dashboard')
    if request.method == "POST":
        form = Loginfrom(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            authenticated_user = authenticate(username=data['username'],password=data['password'])
            if authenticated_user:
                login(request,authenticated_user)
                return redirect('user_agent:dashboard')
    else:
        form = Loginfrom()
    return render(request,'login.html',context={'form':form})

def register(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    if request.method == "POST":
        form = Registerfrom(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'],password=data['password'])
            authenticated_user = authenticate(username=data['username'],password=data['password'])
            if authenticated_user:
                login(request,authenticated_user)
            return redirect('/dashboard')

    else:
        form = Registerfrom()
    return render(request,'register.html',context={'form':form})

