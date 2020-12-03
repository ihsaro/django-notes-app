from authentication.decorators import allowed_groups
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import Note
from .selectors import get_current_client_notes_list, get_current_client_notes_detail
from .services import create_new_note_for_current_user, update_existing_note_for_current_user


@login_required
@allowed_groups(groups=['customer'])
def list_view(request):
    return render(request, 'notes/list.html', context=get_current_client_notes_list(request=request))


# TO BE REFACTORED IN TEMPLATE IN CASE OF ERROR
@login_required
@allowed_groups(groups=['customer'])
def create_view(request):
    if request.method == 'POST':
        if create_new_note_for_current_user(request=request) is True:
            return redirect('notes:list')
        else:
            return redirect('notes:create')
    else:
        return render(request, 'notes/create.html')


@login_required
@allowed_groups(groups=['customer'])
def update_view(request, note_id):
    if request.method == 'POST':
        if update_existing_note_for_current_user(request=request, note_id=note_id) is True:
            return redirect('notes:list')
        else:
            return render(request, 'notes/create.html', context=get_current_client_notes_detail(request=request,
                                                                                                note_id=note_id))
    else:
        try:
            return render(request, 'notes/create.html', context=get_current_client_notes_detail(request=request,
                                                                                                note_id=note_id))
        except Note.DoesNotExist:
            return redirect('notes:list')


@login_required
@require_POST
@csrf_exempt
def delete_view(request):
    current_user = request.user
    note_id_list = request.POST.getlist('id[]')
    for note_id in note_id_list:
        try:
            note = Note.objects.all().filter(user=current_user).get(pk=note_id)
            note.delete()
        except Note.DoesNotExist:
            pass

    return redirect('notes:list')
