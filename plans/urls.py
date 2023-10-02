from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<int:plan_id>', views.plan_details, name='plan_details'),
    path('<plan_id>/<day_id>', views.day, name='day'),
    path('complete/<plan_id>/<day_id>', views.complete, name='complete'),
    path('edit/<int:plan_id>/', views.edit_plan, name='edit_plan'),
    path('delete/<int:plan_id>/', views.delete_plan, name='delete_plan'),
    path('editctegory/<int:category_id>/', views.edit_category, name='edit_category'),
    path('deletecategory/<int:category_id>/', views.delete_category, name='delete_category'),
    path('days', views.days, name='days'),
    path('editday/<int:day_id>/', views.edit_day, name='edit_day'),
    path('deleteday/<int:day_id>/', views.delete_day, name='delete_day'),
]
