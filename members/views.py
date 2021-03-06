from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

# Create your views here.
from .models import Members 





def withdraw(request):
    
    import requests

    from urllib.request import urlopen
    import json
    
    response = urlopen("https://api.coinhive.com/user/balance?name=" + request.user.username + "&secret=97tEENX9hYZoMj6AbKFHYzEYCx7WRk9R")
    
    getdata = json.load(response)
        
    members = Members.objects.get(user_name = request.user.username)
    
    url= "https://api.coinhive.com/user/withdraw"
    data = {}
    data["name"] = request.user.username
    data["secret"] = "97tEENX9hYZoMj6AbKFHYzEYCx7WRk9R"


    template = "withdraw.html" 


    if request.method=='GET': 
        return render(request, template) 
    else:
        

                    
        if float(getdata['balance']) >= float(request.POST["amount"]) and getdata['balance'] != 0:
            
            data["amount"] = request.POST["amount"]
            members.points = float(members.points) + float(request.POST["amount"])
            
            members.save()
            requests.post(url, data=data)

        else:
            return redirect('members:profile')

    return redirect('members:profile')
    

def buy(request):
    
    members = Members.objects.get(user_name = request.user.username)
    
    if members.points is not None:
        members.points = float(members.points) + 1
        
    else:
        
        members.points = 0
        members.money = 0        
    
    members.save()
    return redirect('members:profile') 

def profile(request):
    
    from urllib.request import urlopen
    import json
    
    response = urlopen("https://api.coinhive.com/user/balance?name=" + request.user.username + "&secret=97tEENX9hYZoMj6AbKFHYzEYCx7WRk9R")
    
    data = json.load(response)
    
    if not request.user.is_authenticated:
        
        
        return redirect('members:login1')	
     
        
    else:
        mem_create, members_list = Members.objects.get_or_create(user_name = request.user.username)
        mem_create.save()        
        members_list = Members.objects.all().filter(user_name = request.user.username)
        
        template = "users_profile.html" 
        
        return render(request, template, {'members' : members_list, "jsondata" : data})  





def users_home(request): 
    """ 
    Get data from models.py 
    
    """ 
    if not request.user.is_authenticated:
        
        
        return redirect('members:login1')	
     
        
    else:
        users_list = User.objects.all()
        
        template = "users_home.html" 
        
        return render(request, template, {'users' : users_list})  

 

def register(request): 
    """ 
    Get data from models.py 
    """ 
    
    user = User()
    member = Members()
    
    
 
    template = "reg_form.html" 
    if request.method=='GET': 
        return render(request, template) 
    else:
        
        user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
        user.first_name = request.POST["first_name"] 
        user.last_name = request.POST["last_name"]   
                
        member.user_name = request.POST["username"]
#        member.age = request.POST["age"]
#        member.phone = request.POST["phone"]
        
        user.save()
        member.save()
                 
        return redirect('members:users_home')


@csrf_protect
def login1(request): 
    """ 
    Get data from models.py 
    """ 
       
    user = User.objects.all() 
 
    context = { 
        'user' : user 
    } 

 
    template = "users_login.html" 
    if request.method=='GET': 
        return render(request, template, context) 
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
            
            
            return redirect('articles:home')
        else:
            
        
            return redirect('members:register') 


def logout1(request):
    logout(request)
    
    return redirect('articles:home')
    

         
def create(request1): 
    """ 
    Get data from models.py 
    """ 
 
    template = "members_form.html" 
    if request1.method=='GET': 
        return render(request1, template) 
    else: 
 
        member = Members() 
        member.first_name = request1.POST["first_name"] 
        member.last_name = request1.POST["last_name"]
        member.age = request1.POST["age"] 
        member.email = request1.POST["email"]
        member.password = request1.POST["password"]
        
        member.save()
        
         
        return redirect('members:members_home') 
 
def delete(request1, usrId): 
    """ 
    Get data from models.py 
    """ 
 
    usr = User.objects.get(id=usrId) 
    usr.delete() 
    return redirect('members:users_home') 
 
def update(request, usrId): 
    """ 
    Get data from models.py 
    """ 
    
    users = User.objects.get(id=usrId) 
 
    context = { 
        'users' : users 
    } 
 
    template = "update_form.html" 
    if request.method=='GET': 
        return render(request, template, context) 
    else: 

        users.first_name = request.POST["first_name"] 
        users.last_name = request.POST["last_name"]
        users.email = request.POST["email"]
        users.set_password(request.POST["password"])
        users.save()
        
        
        
        return redirect('members:users_home')


def up_profile(request, memId): 
    """ 
    Get data from models.py 
    """ 
    
    members = Members.objects.get(id=memId) 
 
    context = { 
        'members' : members 
    } 
 
    template = "update_profile.html" 
    if request.method=='GET': 
        return render(request, template, context) 
    else:
        
        if members.user_name=='admin':
            
            members.age = request.POST["age"]
            members.phone = request.POST["phone"]
            members.upline = request.POST["upline"]
            members.tin = request.POST["tin"]
            members.points = request.POST["points"]
            members.money = request.POST["money"]
            members.save()
        
        else:
            members.age = request.POST["age"]
            members.phone = request.POST["phone"]
            members.upline = request.POST["upline"]
            members.tin = request.POST["tin"]
            members.save()


            
        
        
        return redirect('members:profile')

        
        
def del_profile(request1, memId): 
    """ 
    Get data from models.py 
    """ 
 
    mem = Members.objects.get(id=memId) 
    mem.delete() 
    return redirect('members:users_home') 
