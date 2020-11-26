from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.decorators import allowed_groups
from notes.models import Note


@login_required
@allowed_groups(groups=['management'])
def list_customers_view(request):
    if request.method == 'GET':

        groups_names = []

        for group in request.user.groups.all():
            groups_names.append(group.name)

        customers = []

        for user in User.objects.all():
            customers.append({
                'user_details': user,
                'number_of_notes': Note.objects.filter(user=user).count()
            })

        context = {
            'customers': customers,
            'groups_names': groups_names
        }
        return render(request, 'management/list_customers.html', context=context)
