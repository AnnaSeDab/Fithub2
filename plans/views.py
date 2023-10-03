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
            messages.info(request, f'You have succesfuly updated { plan.name }!')
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
    messages.info(request, f'Fitness plan {plan.name} has been deleted!')
    return redirect(reverse('plans'))


@login_required
def edit_category(request, category_id):
    """ Edit a fitness plan categry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(PlanCategory, pk=category_id)
    if request.method == 'POST':
        form = FitnessCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.info(request, f'You have succesfuly updated { category.name }!')
            return redirect(reverse('plans'))
        else:
            messages.error(
                request, 'Your atempt to edit a category failed. Please make sure the form is valid.')
    else:
        form = FitnessCategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'plans/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ Delete a fitness category """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(PlanCategory, pk=category_id)
    category.delete()
    messages.info(request, f'Category {category.name} has been deleted!')
    return redirect(reverse('plans'))


@login_required
def days(request):
    """ Display Fitness days. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    days = DayPlan.objects.all()
    form = PlanForm()

    context = {
        'days': days,
        'form': form,
    }

    return render(request, 'plans/days.html', context)

@login_required
def edit_day(request, day_id):
    """ Edit a fitness day plan categry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    day = get_object_or_404(DayPlan, pk=day_id)
    if request.method == 'POST':
        form = DayForm(request.POST, request.FILES, instance=day)
        if form.is_valid():
            form.save()
            messages.info(request, f'You have succesfuly updated { day.name }!')
            return redirect(reverse('days'))
        else:
            messages.error(
                request, 'Your atempt to edit a fitness day failed. Please make sure the form is valid.')
    else:
        form = DayForm(instance=day)
        messages.info(request, f'You are editing {day.name}')

    template = 'plans/edit_day.html'
    context = {
        'form': form,
        'day': day,
    }

    return render(request, template, context)


@login_required
def delete_day(request, day_id):
    """ Delete a fitness day """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    day = get_object_or_404(DayPlan, pk=day_id)
    day.delete()
    messages.info(request, f'Fitness day {day.name} has been deleted!')
    return redirect(reverse('plans'))

