from django.http.request import HttpRequest
from .models import Note


def create_new_note_for_current_user(*, request: HttpRequest) -> bool:
    note = Note(note_title=request.POST['note-title'], note_type=request.POST['note-type'],
                note_description=request.POST['note-description'], user=request.user)
    note.save()
    if note.id is not None:
        return True
    return False


def update_existing_note_for_current_user(*, request: HttpRequest, note_id: int) -> bool:
    note = Note.objects.get(pk=note_id)

    if (note.note_title == request.POST['note-title'] and
            note.note_type == request.POST['note-type'] and
            note.note_description == request.POST['note-description']):
        return False

    note.note_title = request.POST['note-title']
    note.note_type = request.POST['note-type']
    note.note_description = request.POST['note-description']
    note.save()

    return True
