from django.http import HttpRequest


def get_default_route_to_redirect(*, request: HttpRequest) -> str:
    groups_names = []
    for group in request.user.groups.all():
        groups_names.append(group.name)

    if 'customer' in groups_names:
        return 'notes:list'
    elif 'management' in groups_names:
        return 'management:dashboard'
