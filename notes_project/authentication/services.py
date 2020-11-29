from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpRequest


def authenticate_and_login_user(*, request: HttpRequest) -> User:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return User
    return None
