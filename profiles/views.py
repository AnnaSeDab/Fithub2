from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


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

    template = 'profiles/my_plan.html'
    context = {
        'profile': profile,
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
