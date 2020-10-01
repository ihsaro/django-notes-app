from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('update/<int:note_id>/', views.update, name='update'),
]
