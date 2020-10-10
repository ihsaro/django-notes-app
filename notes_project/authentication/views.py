from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notes:list')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'authentication/login.html')
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('notes:list')
    else:
        return render(request, 'authentication/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            context = {
                'username': username
            }
            messages.error(request, 'Passwords do not match')
            return render(request, 'authentication/register.html', context)

        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            messages.success(request, 'Account created successfully, please log in!')
            return render(request, 'authentication/login.html')
        else:
            messages.error(request, 'Error creating account, please try again!')
            return render(request, 'authentication/register.html')
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('notes:list')
    else:
        return render(request, 'authentication/register.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return render(request, 'authentication/login.html')
