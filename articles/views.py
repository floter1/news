from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from django.views.generic import TemplateView



#From Members
#from django.views.decorators.csrf import csrf_protect




# Create your views here.
from .models import Articles
from .models import Bsell
from members.models import Members


def buy_friend(request, fsellId): 
    """ 
    Get data from models.py 
    """ 
    
    myfriend = Bsell.objects.get(id=fsellId)
    myfriend2 = Members.objects.get(user_name=myfriend.user_name)
    
    myself = Bsell.objects.get(user_name=request.user.username)
    myself2 = Members.objects.get(user_name=request.user.username)
    
    prevowner = Bsell.objects.get(user_name=myfriend.owner)
    prevowner2 = Members.objects.get(user_name=myfriend.owner)
    
    share = float(myfriend2.points) * 0.01
    growth = float(myfriend.price) * 0.02
    cost = float(myfriend2.points) + share



    if myfriend.coins is not None:
        
        if myself2.points > cost:
            
            myfriend2.points = float(myfriend2.points) + cost
            myself2.points = float(myself2.points) - cost
            prevowner2.points = float(prevowner2.points) + share
            
            myfriend.price = float(myfriend.price) + growth
            myfriend.owner = request.user.username
            
            myfriend.coins = myfriend2.points            
            myself.coins = myself2.points
            prevowner.coins = prevowner2.points
        
        else:
            return redirect('articles:sell_friends')
        
    else:
        
        myfriend.coins = 0        
    
    myfriend.save()
    myfriend2.save()
    
    myself.save()
    myself2.save()
    
    prevowner.save()
    prevowner2.save()
    
    return redirect('articles:sell_friends') 



def sell_friends(request):
    

    forsale = Bsell.objects.exclude(owner=request.user.username) & Bsell.objects.exclude(user_name=request.user.username)
    myprofile = Bsell.objects.filter(user_name = request.user.username)
    

    
    template = "bsell_home.html"
    context = {
    	"forsale" : forsale, 
    	'myprofile' : myprofile
    	}

    
    return render(request, template, context)



def bsell_profile(request):
    
    
#    bprofile_list = Articles.objects.all()
        
    if not request.user.is_authenticated:
        
        
        return redirect('members:login1')	
     
        
    else:
        bprofile_create, bprofile_list = Bsell.objects.get_or_create(user_name = request.user.username)
        myprofile2 = Members.objects.get(user_name = request.user.username)
        bprofile_create.coins = myprofile2.points

        bprofile_create.save()        
        bprofile_list = Bsell.objects.all().filter(user_name = request.user.username)
        
#        bprofile_list = Bsell.objects.get(user_name = request.user.username)

        
        
        template = "bsell_profile.html" 
        
        context = {
        'bprofiles' : bprofile_list	
        	
        	}
        
        return render(request, template, context)  


def up_bprofile(request, profId): 
    """ 
    Get data from models.py 
    """ 
    
    bprofiles = Bsell.objects.get(id=profId) 
 
    context = { 
        'bprofiles' : bprofiles 
    } 
 
    template = "up_bprofile.html" 
    if request.method=='GET': 
        return render(request, template, context) 
    else:
        
        if bprofiles.user_name=='admin':
            
            bprofiles.user_name = request.POST["user_name"]
            bprofiles.owner = request.POST["owner"]
            bprofiles.coins = request.POST["coins"]
            bprofiles.price = request.POST["price"]
            bprofiles.save()
        
#        else:
            
#            members.save()
        
        return redirect('members:profile')

        
        
def del_bprofile(request1, profId): 
    """ 
    Get data from models.py 
    """ 
 
    prof = Bsell.objects.get(id=profId) 
    prof.delete() 
    return redirect('members:profile') 






def home(request): 
    """ 
    Get data from models.py 
    
    """ 
    if not request.user.is_authenticated:
        
        
        return redirect('members:login1')	
        
    else:
        
        article_list = Articles.objects.all()
        
        template = "home.html" 
        
        context = { 
        	'articles' : article_list 
        	}
        
        return render(request, template, context)
        
        
class header(TemplateView):
    template_name = "html/header.html"

class footer(TemplateView):
    template_name = "html/footer.html"
        
'''
def header(request):
    """
    Get data from models.py
    """
    template = "html/header.html"


    return render(template)

def footer(request):
    """
    Get data from models.py
    """
    template = "html/footer.html"


    return render(request, template)
'''



'''
def home(request):
    """
    Get data from models.py
    """

    article_list = Articles.objects.all()

    template = "home.html"
    context = {
        'articles' : article_list
    }

    return render(request, template, context)
'''


def create(request):
    """
    Get data from models.py
    """

    template = "form.html"
    if request.method=='GET':
        return render(request, template)
    else:

        article = Articles()
        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.writer = request.user.username
#        article.writer = request.POST["writer"]
        article.save()
        return redirect('articles:home')

def delete(request, artId):
    """
    Get data from models.py
    """

    art = Articles.objects.get(id=artId)
    art.delete()
    return redirect('articles:home')

def update(request, artId):
    """
    Get data from models.py
    """

#    art = Articles.objects.get(id=artId)
    article = Articles.objects.get(id=artId)

    context = {
#        'article' : art
        'article' : article
    }

    template = "form.html"
    if request.method=='GET':
        return render(request, template, context)
    else:

    #    article = Articles.objects.get(id=artId)

        article.title = request.POST["title"]
        article.content = request.POST["content"]
        article.save()
        return redirect('articles:home')
