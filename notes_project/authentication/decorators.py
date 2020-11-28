from django.http import HttpResponse
from django.shortcuts import render, redirect


def allowed_groups(groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in groups:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Not authorized to view this page!')
        return wrapper_func
    return decorator


def redirect_to_default_if_authenticated():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated and request.method == 'GET':
                groups_names = []
                for group in request.user.groups.all():
                    groups_names.append(group.name)

                if 'customer' in groups_names:
                    return redirect('notes:list')
                elif 'management' in groups_names:
                    return redirect('management:dashboard')
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
