from django.shortcuts import render, redirect
# Create your views here.


def index_view(request):
    if request.user.is_authenticated:
        return redirect('notes:list')
    else:
        return render(request, 'homepage/index.html')
