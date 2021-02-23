from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

#Login Function
def devlogin(request):
    if request.method == 'POST':
        userName=request.POST['name']
        password =request.POST['password']
        user = authenticate(request,username=userName,password=password)
        user.save()
        if user is not None:
            login(request,user)
            return redirect(reverse('dev_home'))
        else:
            messages.error(request, 'Invalid Username or Password!')
    else:
        return render(request,'Authentication/login.html')

#Registrattion Function
def devregistration(request):
    if request.method == 'POST':
        userName = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=userName).exists():
                messages.error(request,'Username already exist!')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exist!')
            else:
                user = User.objects.create_user(username=userName,password=password,email=email)
                user.save()
                return redirect('login')
        else:
            messages.error(request,'Password and confirm password doesnt match')
    return render(request,'Authentication/registration.html')

def devrecovery(request):
    return render(request,'Authentication/recovery.html')
def devlogout(request):
    logout(request)
    messages.success(request, 'Successfully Logout!!.')
    return redirect('login')