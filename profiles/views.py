from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

from datetime import timedelta, date


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'on_profile_page': True,
    }

    return render(request, template, context)


def my_info(request):
    """ Display the user's profile with user info """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    template = 'profiles/my_info.html'
    context = {
        'form': form,
        'on_profile_page': True,
        'profile': profile,
    }

    return render(request, template, context)


def my_orders(request):
    """ Display the user's profile with user order history"""
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/my_orders.html'
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)


def my_plan(request):
    """ Display the user's profile with user fitness plan """
    profile = get_object_or_404(UserProfile, user=request.user)

    date_now = date.today()
    start_date = profile.fitness_plan.start_day
    profile.fitness_plan.day_one.available_from = start_date
    profile.fitness_plan.day_two.available_from = start_date + timedelta(days=1)
    profile.fitness_plan.day_three.available_from = start_date + timedelta(days=2)
    profile.fitness_plan.day_four.available_from = start_date + timedelta(days=3)
    profile.fitness_plan.day_five.available_from = start_date + timedelta(days=4)
    profile.fitness_plan.day_six.available_from = start_date + timedelta(days=5)
    profile.fitness_plan.day_seven.available_from = start_date + timedelta(days=6)
    profile.fitness_plan.day_eight.available_from = start_date + timedelta(days=7)
    profile.fitness_plan.day_nine.available_from = start_date + timedelta(days=8)
    profile.fitness_plan.day_ten.available_from = start_date + timedelta(days=9)
    profile.fitness_plan.day_eleven.available_from = start_date + timedelta(days=10)
    profile.fitness_plan.day_twelve.available_from = start_date + timedelta(days=11)
    profile.fitness_plan.day_thirteen.available_from = start_date + timedelta(days=12)
    profile.fitness_plan.day_fourteen.available_from = start_date + timedelta(days=13)
    profile.fitness_plan.day_fifteen.available_from = start_date + timedelta(days=14)
    profile.fitness_plan.day_sixteen.available_from = start_date + timedelta(days=15)
    profile.fitness_plan.day_seventeen.available_from = start_date + timedelta(days=16)
    profile.fitness_plan.day_eighteen.available_from = start_date + timedelta(days=17)
    profile.fitness_plan.day_nineteen.available_from = start_date + timedelta(days=18)
    profile.fitness_plan.day_twenty.available_from = start_date + timedelta(days=19)
    profile.fitness_plan.day_twentyone.available_from = start_date + timedelta(days=20)
    profile.fitness_plan.day_twentytwo.available_from = start_date + timedelta(days=21)
    profile.fitness_plan.day_twentythree.available_from = start_date + timedelta(days=22)
    profile.fitness_plan.day_twentyfour.available_from = start_date + timedelta(days=23)
    profile.fitness_plan.day_twentyfive.available_from = start_date + timedelta(days=24)
    profile.fitness_plan.day_twentysix.available_from = start_date + timedelta(days=25)
    profile.fitness_plan.day_twentyseven.available_from = start_date + timedelta(days=26)
    profile.fitness_plan.day_twentyeight.available_from = start_date + timedelta(days=27)

    print(date_now)
    print(profile.fitness_plan.start_day)
    print(profile.fitness_plan.day_one.available_from)
    print(profile.fitness_plan.day_two.available_from)
    print(profile.fitness_plan.day_three.available_from)
    template = 'profiles/my_plan.html'
    context = {
        'profile': profile,
        'date_now': date_now,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
