from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Note


@login_required
def list_view(request):
    current_user = request.user
    context = {
        'notes': Note.objects.all().filter(user=current_user)
    }
    return render(request, 'notes/list.html', context)


@login_required
def create_view(request):
    return render(request, 'notes/create.html')


@login_required
def update_view(request, note_id):
    current_user = request.user
    try:
        context = {
            'note': Note.objects.all().filter(user=current_user).get(pk=note_id)
        }
        return render(request, 'notes/create.html', context)
    except Note.DoesNotExist:
        return redirect('notes:list')
