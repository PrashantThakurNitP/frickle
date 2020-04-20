from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm #import django form
from django.contrib.auth.models import User#help to create user object quickly
#this is user model we would be working with
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate#to make user login after signup
from .forms import TodoForm
from .models import Todo
from django.utils import timezone

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'todo/home.html')

def signupuser(request):
    if request.method== 'GET' : 
        #we need to distinguish betwen when someone do get and post
        #if request method is get we need to return signup page and form like this
        return render(request,"todo/signupuser.html",{'form':UserCreationForm()})
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
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,"todo/signupuser.html",{'form':UserCreationForm(),"error":"username already taken"})
        elif len(lst)>1:
            return render(request,"todo/signupuser.html",{'form':UserCreationForm(),'error':"space not allowed in username"})

        else:
            #print("Password didnot match .Go back and try again")
            return render(request,"todo/signupuser.html",{'form':UserCreationForm(),'error':"password not matching"})
            #tell  the user password donot match
            #create new user


def loginuser(request):
    if request.method== 'GET' : 
        
        return render(request,"todo/loginuser.html",{'form':AuthenticationForm()})
    else:
        user =authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
             return render(request,"todo/loginuser.html",{'form':AuthenticationForm(),'error':"username or password didnot match"})
             #if user is none send them to same page with error
        else:
            #login
            login(request,user) 
            return redirect('currenttodos')


        #authenticate return user object
       #we need to check whether they have given cotrrect username or not
@login_required       
def currenttodos(request):
    todos=Todo.objects.filter(user=request.user,datecompleted__isnull=True)#if we apply .all then for person everyon to do list will be shown

    return render(request,'todo/currenttodos.html',{'todos':todos})
@login_required  
def completedtodos(request):
    todos=Todo.objects.filter(user=request.user,datecompleted__isnull=False).order_by("-datecompleted")
    #it order things based on date complted
    #- sign before datecompleted means completed soon appear on top
    #if we apply .all then for person everyon to do list will be shown

    return render(request,'todo/completedtodos.html',{'todos':todos})
@login_required  
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')#redirect to homepage after logout
@login_required  
def createtodo(request):
    if request.method =="GET": #when user first visit form show the form
        return render(request,"todo/createtodo.html",{'form':TodoForm()})
        
    else:
        try:
               #if length is not large we send save it
               #when he click submit
               #fetch information from post request
               form=TodoForm(request.POST)
               #whatever user sent in post method we cnvert it to TodoForm form ie form
               newtodo=form.save(commit=False) #commit =False means donot unnecessarily save it into database
               #in newtodo user field is missing 
               newtodo.user=request.user
               newtodo.save()#now it put it in database
               #after saving  this we want to send them to current page so that they can see current to do
               return redirect('currenttodos')
        except ValueError:
                #if length of title is long we send back to same page otherwise we will get error
                return render(request,"todo/createtodo.html",{'form':TodoForm(),"error":"bad data"})
@login_required  
def viewtodo(request,todo_pk): #it takes back request and also primary key
    todo=get_object_or_404(Todo,pk=todo_pk,user=request.user) 
     #grab a todo from datbase as we know primary key and classs
     #user is passec as someone else couldnot modify only creator can modify it
    if request.method =='GET':
        form=TodoForm(instance=todo)  # we need to pass in todo object inside TodoForm
        #rather than passing empty form we pass todo object inside form
        return render(request,'todo/viewtodo.html',{'todo':todo,"form":form}) #pass in form
        #we need to display todo form filled in with information
    else:
        #take form data and save it in database
        #if someone save informatio it sending post back to save page
        try:
            form=TodoForm(request.POST,instance=todo)# we pass todo help to determine it is existing object we are updating
            # rather than empty form we pass to do object
            form.save()#if someone save data redirect to currenttodod
            return redirect('currenttodos')
        except ValueError:
            return render(request,'todo/viewtodo.html',{'todo':todo,"form":form,"error":"BAD Info"})

@login_required  
def completetodo(request,todo_pk):
    todo=get_object_or_404(Todo,pk=todo_pk,user=request.user) 
    #we only need to do POST to complete todo
    if request.method== 'POST':
        #then we have to say this todo item has been been completed 
        todo.datecompleted=timezone.now()#we assign present time of marking for dat completed
        #afer assigning time we need to save this object
        todo.save()
        #after that we will send user back to current list of items
        return redirect('currenttodos')
        #we have saved todo and views but it doesnot have template
        #we go to viewtodo and make another form and we must have buttom as complete
@login_required  
def deletetodo(request,todo_pk):
    todo=get_object_or_404(Todo,pk=todo_pk,user=request.user) 
    #we only need to do POST to delete todo
    if request.method== 'POST':
       
        todo.delete()
        #after that we will send user back to current list of items
        return redirect('currenttodos')
        #we have saved todo and views but it doesnot have template
        #we go to viewtodo and make another form and we must have buttom as complete