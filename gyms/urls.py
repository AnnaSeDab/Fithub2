from django.urls import path
from . import views

urlpatterns = [
    path('', views.gyms, name="gyms"),
    path('add/', views.add_gym, name='add_gym'),
    path('edit/<int:gym_id>/', views.edit_gym, name='edit_gym'),
    path('delete/<int:gym_id>/', views.delete_gym, name='delete_gym'),
]
