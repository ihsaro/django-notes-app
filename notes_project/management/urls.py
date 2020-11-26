from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('users/', views.list_customers_view, name='list_customers')
]