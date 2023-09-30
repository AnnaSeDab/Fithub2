from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('my_info', views.my_info, name='my_info'),
    path('my_plan', views.my_plan, name='my_plan'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]
