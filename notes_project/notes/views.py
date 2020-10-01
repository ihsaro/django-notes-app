from django.shortcuts import render

# Create your views here.


def list(request):
    return render(request, 'notes/list.html')


def create(request):
    return render(request, 'notes/list.html')


def update(request, note_id):
    return render(request, 'notes/list.html')
