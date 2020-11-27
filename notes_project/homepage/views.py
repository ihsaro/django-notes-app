from django.shortcuts import render, redirect
# Create your views here.


def index_view(request):
    groups_names = []
    for group in request.user.groups.all():
        groups_names.append(group.name)

    if request.user.is_authenticated and 'customer' in groups_names:
        return redirect('notes:list')
    elif request.user.is_authenticated and 'management' in groups_names:
        return redirect('management:dashboard')
    else:
        return render(request, 'homepage/index.html')
