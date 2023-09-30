from django.shortcuts import render, get_object_or_404


from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def my_info(request):
    """ Display the user's profile with user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/my_info.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def my_orders(request):
    """ Display the user's profile with user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/my_orders.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def my_plan(request):
    """ Display the user's profile with user profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/my_plan.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
