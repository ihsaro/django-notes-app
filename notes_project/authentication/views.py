from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .decorators import redirect_to_default_if_authenticated
from .selectors import get_default_route_to_redirect
from .services import authenticate_and_login_user, validate_password_match, create_user, logout_user


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
        if validate_password_match(request=request) is False:
            context = {
                'username': request.POST['username']
            }
            messages.error(request, 'Passwords do not match')
            return render(request, 'authentication/register.html', context)

        if create_user(request=request) is not None:
            messages.success(request, 'Account created successfully, please log in!')
            return render(request, 'authentication/login.html')
        else:
            messages.error(request, 'Error creating account, please try again!')
            return render(request, 'authentication/register.html')
    elif request.method == 'GET':
        return render(request, 'authentication/register.html')


def logout_view(request):
    if logout_user(request=request) is True:
        messages.success(request, 'Logout Successful')
    else:
        messages.warning(request, 'No user is logged in, please log in or create an account to continue!')
    return render(request, 'authentication/login.html')
