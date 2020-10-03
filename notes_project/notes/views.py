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
    if request.method == 'POST':
        note_title = request.POST['note-title']
        note_type = request.POST['note-type']
        note_description = request.POST['note-description']

        note = Note(note_title=note_title, note_type=note_type,
                    note_description=note_description, user=request.user)
        note.save()
        if note.id is not None:
            return redirect('notes:list')
        else:
            return redirect('notes:create')
    else:
        return render(request, 'notes/create.html')


@login_required
def update_view(request, note_id):
    if request.method == 'POST':
        note_title = request.POST['note-title']
        note_type = request.POST['note-type']
        note_description = request.POST['note-description']

        note = Note.objects.get(pk=note_id)
        note.note_title = note_title
        note.note_type = note_type
        note.note_description = note_description
        note.save()

        return redirect('notes:list')
    else:
        current_user = request.user
        try:
            context = {
                'note': Note.objects.all().filter(user=current_user).get(pk=note_id)
            }
            return render(request, 'notes/create.html', context)
        except Note.DoesNotExist:
            return redirect('notes:list')
