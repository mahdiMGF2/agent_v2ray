from django.db.models import Sum
from django.shortcuts import render,redirect
from .forms import Loginfrom,Registerfrom
from django.contrib.auth import login,authenticate
from .models import User,UserAgent,Account_agent
# Create your views here.

def Dashboard(request):
    if str(request.user) == "AnonymousUser":
        return redirect('/login')
    Acoount = UserAgent.objects.get(user=request.user)
    Sum_volume = Account_agent.objects.filter(user=request.user).aggregate(Sum=Sum('volume'))
    Count_user = Account_agent.objects.filter(user=request.user).count()
    data_transfer = {
        "account_info": Acoount,
        "sum_volume": Sum_volume,
        "count_user": Count_user,
    }
    return render(request,'dashboard.html',context=data_transfer)


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