from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.decorators import allowed_groups


@login_required
@allowed_groups(groups=['management'])
def list_customers_view(request):
    if request.method == 'GET':

        groups_names = []

        for group in request.user.groups.all():
            groups_names.append(group.name)

        context = {
            'customers': User.objects.filter(groups__name='customer'),
            'groups_names': groups_names
        }
        return render(request, 'management/list_customers.html', context=context)
