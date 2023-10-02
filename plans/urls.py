from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<plan_id>', views.plan_details, name='plan_details'),
    path('<plan_id>/<day_id>', views.day, name='day'),
    path('complete/<plan_id>/<day_id>', views.complete, name='complete'),
    path('edit/<int:plan_id>/', views.edit_plan, name='edit_plan'),
    path('delete/<int:plan_id>/', views.delete_plan, name='delete_plan'),
]
