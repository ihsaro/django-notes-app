from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list(request):
    return render(request, 'notes/list.html')


@login_required
def create(request):
    return render(request, 'notes/list.html')


@login_required
def update(request, note_id):
    return render(request, 'notes/list.html')
