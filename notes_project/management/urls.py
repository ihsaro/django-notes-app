from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    # path('users/', views.list_customers_view, name='list_customers')
]