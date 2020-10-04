from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.list_view, name='list'),
    path('create/', views.create_view, name='create'),
    path('update/<int:note_id>/', views.update_view, name='update'),
    path('delete/', views.delete_view, name='delete'),
]
