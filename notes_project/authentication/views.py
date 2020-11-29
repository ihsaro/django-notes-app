from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .decorators import redirect_to_default_if_authenticated
from .selectors import get_default_route_to_redirect
from .services import authenticate_and_login_user


@redirect_to_default_if_authenticated()
def login_view(request):
    if request.method == 'POST':
        if authenticate_and_login_user(request=request) is not None:
            return redirect(get_default_route_to_redirect(request=request))
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'authentication/login.html')
    elif request.method == 'GET':
        return render(request, 'authentication/login.html')


@redirect_to_default_if_authenticated()
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
    elif request.method == 'GET':
        return render(request, 'authentication/register.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logout Successful')
    else:
        messages.warning(request, 'No user is logged in, please log in or create an account to continue!')
    return render(request, 'authentication/login.html')
