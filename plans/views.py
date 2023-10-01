from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import DayPlan, FitnessPlan, PlanCategory
from merchandise.models import Product, Category

from .forms import PlanForm


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


def complete(request, plan_id, day_id):
    """A view to return the page after finishing the workout """

    plan = get_object_or_404(FitnessPlan, pk=plan_id)
    day = get_object_or_404(DayPlan, pk=day_id)

    print(day)
    day.completed = True
    day.save(update_fields=['completed'])

    context = {
        'day': day,
    }

    return render(request, 'plans/complete.html', context)


@login_required
def add_plan(request):
    """ Add a new fitness plan to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have added new fitness plan!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Your atempt to add a product failed. Please make sure the form is valid.')
    else:
        form = PlanForm()
        
    template = 'plans/add_plan.html'
    context = {
        'form': form,
    }

    return render(request, template, context)