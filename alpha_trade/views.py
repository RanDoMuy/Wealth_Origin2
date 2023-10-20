from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import User, Deposit_History, Investment_Plan, Withdrawal_History
import time

# Create your views here.

def handler404(requests, exception):
    return HttpResponseRedirect('/home/')

def load(requests):
    return render(requests, "load.html")

def home(requests):
    return render(requests, "home.html")

def about(requests):
    return render(requests, "about.html")

def terms(requests):
    return render(requests, "terms.html")

def register(requests):
    if requests.method== "POST":
        fullname= requests.POST["fullname"]
        email= requests.POST["email"]
        number= requests.POST["number"]
        country= requests.POST["country"]
        password= requests.POST["password"]
        password2= requests.POST["password2"]
        country= requests.POST["country"]
        try:
            if password2==password:
                user = User.objects.create_user(full_name=fullname, email=email, password=password, passwd= password2, number= number, country=country)
                user.save()
                user = authenticate(requests, email=email, password=password)
                login(requests, user)
                return redirect("dashboard")   
            else:
                error_message= "Passwords do not match"
                return render(requests, "register.html", {"error_message":error_message})
        except:
            redirect("home")
    return render(requests, "register.html")

def user_login(requests):
    if requests.method=="POST":
        email = requests.POST['email']
        password = requests.POST['password']
        user= authenticate(requests, email=email, password=password)
    
        if user is not None:
            login(requests, user)
            return redirect("dashboard")
                
        else:
            error_message= "Invalid Username or Password"
            return render(requests, "login.html", {"error_message":error_message})
    return render(requests, "login.html")

@login_required(login_url='/accounts/login/')
def dashboard(requests):
    user = requests.user
    if user.verify == False:
        message= "Verify Your Account"
        dd= "block"
        if requests.method == 'POST' and 'image' in requests.FILES:
            Image = requests.FILES['image']
        
            imager= User(image= Image)

            imager.save()
            user.verify= True

            user.save()
            dd= "none"
            return render(requests, "dashboard.html", {'user': user, 'dd':dd})
        return render(requests, "dashboard.html", {'user': user, 'message': message, 'dd':dd})
    else:
        dd= "none"
        return render(requests, "dashboard.html", {'user': user, 'dd':dd})

@login_required(login_url='/accounts/login/')
def deposit(requests):
    user = requests.user
    deposits = Deposit_History.objects.filter(user=requests.user).order_by('-timestamp')
    if requests.method == 'POST':
        amount = requests.POST['amount']
        deposit = Deposit_History(user=requests.user, amount=amount)
        deposit.save()
        time.sleep(5)
    return render(requests, "deposit.html", {'user': user, 'deposits': deposits})

@login_required(login_url='/accounts/login/')
def invest(requests):
    user = requests.user
    return render(requests, "invest.html",{'user': user})

@login_required(login_url='/accounts/login/')
def starter(requests):
    price= 200
    user= requests.user
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "Starter"
        user.trade_status = "Active"
        user.save()
        return redirect("dashboard")
    else:
        return redirect("invest")

@login_required(login_url='/accounts/login/')
def bronze(requests):
    price= 500
    user= requests.user
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "Bronze"
        user.trade_status = "Active"
        user.save()
        return redirect("dashboard")
    else:
        return redirect("invest")

@login_required(login_url='/accounts/login/')
def silver(requests):
    price= 1000
    user= requests.user
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "Silver"
        user.trade_status = "Active"
        user.save()
        return redirect("dashboard")
    else:
        return redirect("invest")

@login_required(login_url='/accounts/login/')
def gold(requests):
    price= 2000
    user= requests.user
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "Gold"
        user.trade_status= "Active"
        user.save()
        return redirect("dashboard")
    else:
        return redirect("invest")

@login_required(login_url='/accounts/login/')
def diamond(requests):
    price= 5000
    user= requests.user
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "Diamond"
        user.trade_status= "Active"
        user.save()
        return redirect("dashboard")
    else:
        return redirect("invest")

@login_required(login_url='/accounts/login/')
def platinum(requests):
    price= 10000
    user= requests.user
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "Platinum"
        user.trade_status= "Active"
        user.save()
        return redirect("dashboard")
    else:
        return redirect("invest")
 

@login_required(login_url='/accounts/login/')
def withdraw(requests):
    user = requests.user
    withdraws = Withdrawal_History.objects.filter(user=requests.user).order_by('-timestamp')
    if requests.method == 'POST':
        amount = requests.POST['amount']
        withdraw = Withdrawal_History(user=requests.user, amount=amount)
        withdraw.save()
        time.sleep(5)
    return render(requests, "withdraw.html", {'user': user, 'withdraws': withdraws})

@login_required(login_url='/accounts/login/')
def faq(requests):
    user = requests.user
    return render(requests, "faq.html", {'user': user})

@login_required(login_url='/accounts/login/')
def profile(requests):
    user = requests.user
    return render(requests, "profile.html", {'user': user})

@login_required(login_url='/accounts/login/')
def user_logout(requests):
    logout(requests)
    return redirect("home")
