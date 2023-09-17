from django.urls import path
from . import views

urlpatterns = [
    path('', views.merchandise, name="merchandise"),
    path('<product_id>', views.product_detail, name='product_detail'),
]