from django.http import HttpRequest
from django.contrib.auth.models import User
from notes.models import Note
from typing import Any


def get_dashboard_context(*, request: HttpRequest) -> Any:
    groups_names = []
    notes_monthly_count = [
        {
            'month_name': 'January',
            'notes_count': 0
        },
        {
            'month_name': 'February',
            'notes_count': 0
        },
        {
            'month_name': 'March',
            'notes_count': 0
        },
        {
            'month_name': 'April',
            'notes_count': 0
        },
        {
            'month_name': 'May',
            'notes_count': 0
        },
        {
            'month_name': 'June',
            'notes_count': 0
        },
        {
            'month_name': 'July',
            'notes_count': 0
        },
        {
            'month_name': 'August',
            'notes_count': 0
        },
        {
            'month_name': 'September',
            'notes_count': 0
        },
        {
            'month_name': 'October',
            'notes_count': 0
        },
        {
            'month_name': 'November',
            'notes_count': 0
        },
        {
            'month_name': 'December',
            'notes_count': 0
        }
    ]

    for group in request.user.groups.all():
        groups_names.append(group.name)

    for note in Note.objects.all():
        for note_monthly_count in notes_monthly_count:
            if note.created_date.strftime("%B") == note_monthly_count['month_name']:
                note_monthly_count['notes_count'] += 1

    context = {
        'groups_names': groups_names,
        'number_of_customers': User.objects.filter(groups__name='customer').count(),
        'number_of_notes': Note.objects.count(),
        'global_js_properties': {
            'notes_monthly_count': notes_monthly_count,
        },
    }

    return context
