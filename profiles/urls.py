from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('my_info', views.my_info, name='my_info'),
    path('my_plan', views.my_plan, name='my_plan'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('management', views.management, name='management'),
    path('management/add_plan/', views.add_plan, name='add_plan'),
    path('management/add_day/', views.add_day, name='add_day'),
    path('management/add_fitness_category/', views.add_fitness_category, name='add_fitness_category'),
]
