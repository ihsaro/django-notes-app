var deletedNotes = {
    'id': []
};

function addDeletedNote(id) {
    if (!deletedNotes['id'].includes(id)) {
        deletedNotes['id'].push(id);
        document.getElementById('note_delete_' + id).classList.remove('fa-trash-alt');
        document.getElementById('note_delete_' + id).classList.add('fa-times-circle');
    }
    else {
        deletedNotes['id'] = deletedNotes['id'].filter((value, index, array) => {
            return value != id
        });
        document.getElementById('note_delete_' + id).classList.remove('fa-times-circle');
        document.getElementById('note_delete_' + id).classList.add('fa-trash-alt');
    }
}

function batchDeleteNotes(url) {
    $.post(url, deletedNotes);
    location.reload();
}