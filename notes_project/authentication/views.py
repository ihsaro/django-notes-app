from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

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
            return redirect('authentication:login')
    elif request.method == 'GET' and request.user.is_authenticated:
        return redirect('notes:list')
    else:
        return render(request, 'authentication/login.html')


def register_view(request):
    return render(request, 'authentication/register.html')


def logout_view(request):
    logout(request)
    return redirect('authentication:login')
