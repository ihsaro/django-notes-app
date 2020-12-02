from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from authentication.decorators import allowed_groups
from .selectors import get_dashboard_context


@login_required
@allowed_groups(groups=['management'])
@require_http_methods(['GET'])
def dashboard_view(request):
    return render(request, 'management/dashboard.html', context=get_dashboard_context(request=request))
