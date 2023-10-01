from django.shortcuts import render

from .models import Gym


def gyms(request):
    """A view to return the gyms page"""
    return render(request, 'gyms/gyms.html')
