from django.http import HttpRequest
from notes.models import Note
from typing import Any


def get_current_client_notes_list(*, request: HttpRequest) -> Any:
    return {
        'notes': Note.objects.all().filter(user=request.user)
    }


def get_current_client_notes_detail(*, request: HttpRequest, note_id: int) -> Any:
    return {
        'note': Note.objects.all().filter(user=request.user).get(pk=note_id)
    }
