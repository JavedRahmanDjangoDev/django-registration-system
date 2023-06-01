from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method != 'POST':
        return render (request,'signup.html')
    uname=request.POST.get('username')
    email=request.POST.get('email')
    pass1=request.POST.get('password1')
    pass2=request.POST.get('password2')

    if pass1 != pass2:
        return HttpResponse("Your password and confrom password are not Same!!")
    my_user=User.objects.create_user(uname,email,pass1)
    my_user.save()
    return redirect('login')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is None:
            return HttpResponse ("Username or Password is incorrect!!!")

        login(request,user)
        return redirect('home')
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')