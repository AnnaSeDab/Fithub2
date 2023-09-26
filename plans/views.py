from django.shortcuts import render, get_object_or_404

from .models import DayPlan, FitnessPlan, PlanCategory
from merchandise.models import Product, Category


def plans(request):
    """ Display Fitness plans. """

    plans = FitnessPlan.objects.all()
    categories = PlanCategory.objects.all()

    context = {
        'plans': plans,
        'categories': categories,
    }

    return render(request, 'plans/plans.html', context)
