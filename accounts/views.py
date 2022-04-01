from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import RegisterForm


#user registration view
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('register successfull')
            messages.success(request,'Account Created Successfully')
            return redirect('login')

    else:
        form = RegisterForm()

    context = {
        'form' : form
    }
    
    return render(request,'accounts/register.html',context)


#user login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            print('login successfull')
            messages.success(request,'Login successfully')
            return redirect('home')

    return render(request,'accounts/login.html')


#user logout view
def logout_view(request):
    logout(request)
    return redirect('login')
