from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<plan_id>', views.plan_details, name='plan_details'),
    path('<plan_id>/<day_id>', views.day, name='day'),
]
