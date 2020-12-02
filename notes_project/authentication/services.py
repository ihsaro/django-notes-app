from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest


def authenticate_and_login_user(*, request: HttpRequest) -> User:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return User
    return None


def validate_password_match(*, request: HttpRequest) -> bool:
    return request.POST['password'] == request.POST['confirm-password']


def create_user(*, request: HttpRequest) -> User:
    return User.objects.create_user(username=request.POST['username'], password=request.POST['password'])

def logout_user(*, request: HttpRequest) -> bool:
    if request.user.is_authenticated:
        logout(request)
        return True
    else:
        return False
