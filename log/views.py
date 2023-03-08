from django.shortcuts import render,HttpResponse,redirect #shortcuts which are inbuilt to render the page on the browser,give a response and redirect to our destination page
from django.contrib.auth.models import User #autehntictaion models-authenticate the user
from django.contrib.auth import authenticate #authenticate-method to perform the comparison and check to validate user
from django.contrib.auth import login as auth_login # importing as auth_login to use a variable further in the code 
from django.contrib.auth import logout as auth_logout 
from .models import Contact


def home(request): #creating a function to request home page
    return render(request,'index.html') #render the home page ie index.html
def register(request): #requesting the register page
    if request.method=='POST': #to give the inputs taken from the user to the backend from the following variables basically authentication
        uname=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')

        if password!=password1:
            return HttpResponse("Password does not match")#if password dont match this is validation
        else:
             my_user=User.objects.create_user(uname,email,password) #else redirect to login once the details are saved
             my_user.save()
             return redirect('login')


       

        # print(uname,email,password,password1)

    return render(request,'register.html') 
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is wrong")
    return render(request,'login.html')

def aboutus(request):
    return render(request,'AboutUs.html')

def contact(request):
     if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request. POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return render(request,'contact.html')
     
     return render(request,'contact.html')
   
def blog(request):
    return render(request,'Blog.html')

def temp(request):
    return render(request,'temp.html')

def B1(request):
    return render(request,'B1.html')

def B1A(request):
    return render(request,'B1A.html')

def B1B(request):
    return render(request,'B1B.html')
def B2(request):
    return render(request,'B2.html')

def B3(request):
    return render(request,'B3.html')

def B4(request):
    return render(request,'B4.html')

def B5(request):
    return render(request,'B5.html')

def B6(request):
    return render(request,'B6.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def cert(request):
    return render(request,'cert.html')






