from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first name']
        second_name = request.POST['second name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username exists')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists...')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=second_name, username=username, email=email, password=password1)
                user.save()
                messages.info(request,'signup successful!')
                return redirect('signin')
                
        else:
            messages.info(request, 'password does not match...')
            return redirect ('signup')
            
            
        
    return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.info(request,'login successful!')
            return redirect('/')
            
        else:
            messages.info(request, 'invalid details')
            return redirect('signin')
        
    else:
        return render(request, 'signin.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('signin')