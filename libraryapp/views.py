# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from libraryapp.forms import Userform
from libraryapp.forms import LoginForm
from libraryapp.forms import Queryform
from libraryapp.models import Bookdata
from libraryapp.models import login_users
def user_register(request):  #Register the new user
    if request.method == "POST":  
        form = Userform(request.POST)  
        if form.is_valid():  
            try:
                userObj = form.cleaned_data
                username = userObj['username']
                email =  userObj['email']
                password =  userObj['password']
                if (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    messages.success(request, 'Username or Email address already exists')
                    return render(request, 'index.html')
                elif not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)
                    messages.success(request, 'Details are registered successfully!!! You can login')
                    return render(request, 'index.html')
                else:
                    messages.error(request, 'Unexpected error occured!!!')
                    return redirect("/index")
            except:  
                  messages.error(request, 'Registration failed')
                  return redirect("/index")
    else:  
        form = Userform()
    return render(request,'index.html',{'form':form})

def addingbooks(request): #shows all the library database books
    showbooks = Bookdata.objects.all()  
    return render(request,"addbook.html",{'showbooks':showbooks})

def viewbooks(request):  #displays the books taken by the login users
    add_book_view = login_users.objects.filter(user_id=request.user.id) 
    return render(request,"view_book.html",{'add_book_view':add_book_view})

def sucess(request):    
    return render(request,"sucess.html")

def welcome(request):  #After login, displays the users homepage  
    return render(request,"welcome.html")


def login_check(request): #checks the login using inbuilt authentication
    if request.method == "POST":  
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
        # success
            return render(request, 'welcome.html')
        else:
      # invalid login
            messages.error(request, 'Username/Password are incorrect or blank!!!')
            return redirect("/login")
    else:
        return render (request,'login.html')

def Add(request,book_id,book_name,book_publisher,req_user): #Add the books respective to login users
    if (login_users.objects.filter(book_id=book_id).exists()):
        messages.success(request, 'This book already taken!!!')
        return redirect("/addbook")
    else:
        try:
            p1 = login_users.objects.create(book_id=book_id, book_names=book_name,book_publisher=book_publisher,user_id=req_user)  
            messages.success(request, 'Book added successfully!!!')
            #return render(request, 'addbook.html')
            return redirect("/addbook")
        except:
            messages.error(request, 'Operation Failed!!!')
            return redirect("/addbook")


def returned(request,id): #returns the books respective to login users
    try:  
        p2 = login_users.objects.get(id=id)
        p2.delete()
        messages.success(request, 'Book returned successfully!!!')            
        return redirect("/view_book")
    except:
        messages.error(request, 'Operation Failed!!!')
        return redirect("/view_book")

def user_querying(request):  #Query form
    if request.method == "POST":  
        form = Queryform(request.POST)  
        if form.is_valid():  
            try:
                form.save()
                messages.success(request, 'Thanks for your query, will contact you soon!!!') 
                return redirect('/query')  
            except:  
                messages.success(request, 'Something went wrong!!!') 
                return redirect('/query')   
    else:  
        form = Queryform()  
    return render(request,'query.html',{'form':form})  

def logout_view(request):
    logout(request)   
    return render(request,"logout.html")