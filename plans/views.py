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


def plan_details(request, plan_id):
    """A view to return the page with chosen plan details"""

    plan = get_object_or_404(FitnessPlan, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_details.html', context)


def day(request, plan_id, day_id):
    """A view to return the page with chosen day details"""

    plan = get_object_or_404(FitnessPlan, pk=plan_id)
    day = get_object_or_404(DayPlan, pk=day_id)

    context = {
        'plan': plan,
        'day': day,
    }

    return render(request, 'plans/day.html', context)
