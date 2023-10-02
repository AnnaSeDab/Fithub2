from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from .models import DayPlan, FitnessPlan, PlanCategory
from merchandise.models import Product, Category
from profiles.forms import PlanForm, DayForm, FitnessCategoryForm


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
    user = get_object_or_404(UserProfile, user=request.user)
    
    if user.fitness_plan == plan:
        day.completed = True
        day.save(update_fields=['completed'])

        context = {
            'day': day,
        }

        return render(request, 'plans/complete.html', context)
    
    else:
        context = {
            'plan': plan,
        }

        return render(request, 'plans/plan_details.html', context)


@login_required
def edit_plan(request, plan_id):
    """ Edit a fitness plan """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    plan = get_object_or_404(FitnessPlan, pk=plan_id)
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have succesfuly updated { plan.name }!')
            return redirect(reverse('plan_details', args=[plan.id]))
        else:
            messages.error(
                request, 'Your atempt to edit a fitness plan failed. Please make sure the form is valid.')
    else:
        form = PlanForm(instance=plan)
        messages.info(request, f'You are editing {plan.name}')

    template = 'plans/edit_plan.html'
    context = {
        'form': form,
        'plan': plan,
    }

    return render(request, template, context)


@login_required
def delete_plan(request, plan_id):
    """ Delete a fitness plan from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    plan = get_object_or_404(FitnessPlan, pk=plan_id)
    plan.delete()
    messages.success(request, f'Fitness plan {plan.name} has been deleted!')
    return redirect(reverse('plans'))
