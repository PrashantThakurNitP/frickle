
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib.auth.models import User#help to create user object quickly
#this is user model we would be working with
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login,logout ,authenticate#to make user login after signup
from .forms import feedsForm
from .models import feedsModel

from django.shortcuts import render,redirect, get_object_or_404
#import django form

from django.utils import timezone

from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request,"posts/home.html",{"hello":"meassage"})
@login_required
def feeds(request):
    feeds1=feedsModel.objects.all()#if we apply .all then for person everyon to do list will be shown

    
    return render(request,"posts/feeds.html",{"feeds":feeds1})
@login_required
def upvote(request,id1,up):
    #feedsModel.objects.filter(pk=request.pk).update(upvote = upvote+1)
    #obj=get_object_or_404(feedsModel,id=id1,user=request.user_new)
    obj=feedsModel.objects.get(pk=id1)
    s1=str(up)
    sall=str(obj.upvoter)
    #sall=sall+"?"
    ulist=sall.split()
    if s1 in ulist:
        #return render(request,"feeds.html",{"upvoter":request.user.username})
        return redirect("feeds")
        #pass
    else:
    #upvoterlist=txt.split("{")
    
        obj.upvote+=1
        sall=sall+' '
        sall=sall+s1
        obj.upvoter=sall
        
    obj.save()
    #s = get_object_or_404(feedsModel,  pk=question_id)
    #s.upvote+=1 
    #s.save(update_fields=["upvote"]) 
    return redirect("feeds")
    #return render(request,"posts/error.html",{"upvoter":request.user.username,"ulist":ulist})
    #return redirect('feeds')

@login_required
def delete(request,id1):
    #feedsModel.objects.filter(pk=request.pk).update(upvote = upvote+1)
    #obj=get_object_or_404(feedsModel,id=id1,user=request.user_new)
    obj=feedsModel.objects.get(pk=id1)
    if request.method== 'POST':
       
        obj.delete()
        #after that we will send user back to current list of items
        

    
    return redirect('feeds')



# Create your views here.
@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')#redirect to homepage after logout
    else:
        return redirect('loginuser')

def signupuser(request):
    if request.method== 'GET' : 
        #we need to distinguish betwen when someone do get and post
        #if request method is get we need to return signup page and form like this
        return render(request,"posts/signupuser.html",{'form':UserCreationForm()})
        #anytime someone put url in web and hit eneter then he is guest
        #in that time we get request
        #we need to present webpage only in this case
    else:
        #create new user
        #POST method is always from form
        #when someone fill form and click submit in that case we need to save the 
        #user in data base
        # we don't need to create user model
        #there is already the auth app , ie is present in setting
        #hence there is user app already been saved in database
        #********************************************************************
        #when someone has done post to us we need to create that user object

        str1=str(request.POST['username'])
        lst=str1.split()
        if request.POST['password1']==request.POST['password2'] and len(lst)==1: #
            #first we need to verify first and second password
            #if password match then go and create user object 
            try:
                user=User.objects.create_user( username=request.POST['username'], password=request.POST['password1'] )
                #this is function that django has made which make it easy to create new 
                #user object.  Inside this we pass username and password
                #request.POST is like dictionary
                #in user ,name that is going to submit is username , password1  and password2
                user.save()  #user is object and we need to save it in database
                login(request,user) #make them login after they sign in
                #after sigin we take them them to current page which show current to do page
                return redirect('feeds')
            except IntegrityError:
         
                return render(request,"posts/signupuser.html",{'form':UserCreationForm(),"error":"username already taken"})
        elif len(lst)>1:
            return render(request,"posts/signupuser.html",{'form':UserCreationForm(),'error':"space not allowed in username"})
        else:
            #print("Password didnot match .Go back and try again")
            return render(request,"posts/signupuser.html",{'form':UserCreationForm(),'error':"password not matching"})
            #tell  the user password donot match
            #create new user



"""
def loginuser(request):
    if request.method== 'POST' : 
        return render(request,"posts/loginuser.html",{"user":request.POST['username']})
        #return render(request,"posts/loginuser.html",{'form':AuthenticationForm()})
    else:
        return render(request,"posts/loginuser.html",{'form':AuthenticationForm()})
        #user=authenticate(request,username=request.POST['username'], password=request.POST['password'],{"user":request.POST['username']})
        if user is None:
             return render(request,"posts/loginuser.html",{'form':AuthenticationForm(),'error':"username or password didnot match"})
             #if user is none send them to same page with error
        else:
            #login
            login(request,user) 
            return redirect('feeds')

"""

def loginuser(request):
    if request.method== 'GET' : 
        
        return render(request,"posts/loginuser.html",{'form':AuthenticationForm()})
    else:
        user =authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request,"posts/loginuser.html",{'form':AuthenticationForm(),'error':"username or password didnot match"})
             #if user is none send them to same page with error
        else:
            #login
            login(request,user) 
            return redirect('feeds')
@login_required
def addpost(request):
    if request.method =="GET": #when user first visit form show the form
        return render(request,"posts/addpost.html",{'form':feedsForm()})
        
    else:
        try:
               #if length is not large we send save it
               #when he click submit
               #fetch information from post request
               form=feedsForm(request.POST,request.FILES)
               
               newtodo=form.save(commit=False) 




               #whatever user sent in post method we cnvert it to TodoForm form ie form
               #newtodo=form.save(commit=False) #commit =False means donot unnecessarily save it into database
               #in newtodo user field is missing 
               if request.user.is_authenticated:
                        newtodo.user_new=request.user
               newtodo.save()#now it put it in database
               #return render(request,"posts/error.html",{"form2":form})
               #after saving  this we want to send them to current page so that they can see current to do
               return redirect('feeds')
        except ValueError:
                #if length of title is long we send back to same page otherwise we will get error
                return render(request,"posts/addpost.html",{'form':feedsForm()})
                #               ,"error1":"bad data","user1":request.user,"form1":newtodo




        #authenticate return user object
       #we need to check whether they have given cotrrect username or not
        #authenticate return user object
       #we need to check whether they have given cotrrect username or not
       
