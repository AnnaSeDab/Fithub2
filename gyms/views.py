from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Gym
from .forms import GymForm


def gyms(request):
    """A view to return the gyms page"""

    gyms = Gym.objects.all()

    context = {
        'gyms': gyms,
    }

    return render(request, 'gyms/gyms.html', context)

@login_required
def edit_gym(request, gym_id):
    """ Edit a gym  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    gym = get_object_or_404(Gym, pk=gym_id)
    if request.method == 'POST':
        form = GymForm(request.POST, request.FILES, instance=gym)
        if form.is_valid():
            form.save()
            messages.info(request, f'You have succesfuly updated { gym.name }!')
            return redirect(reverse('gyms'))
        else:
            messages.error(
                request, 'Your atempt to edit a Gym failed. Please make sure the form is valid.')
    else:
        form = GymForm(instance=gym)
        messages.info(request, f'You are editing {gym.name}')

    template = 'gyms/edit_gym.html'
    context = {
        'form': form,
        'gym': gym,
    }

    return render(request, template, context)


@login_required
def delete_gym(request, gym_id):
    """ Delete a Gym from the page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    gym = get_object_or_404(Gym, pk=gym_id)
    gym.delete()
    messages.info(request, f'Gym {gym.name} has been deleted!')
    return redirect(reverse('gyms'))


@login_required
def add_gym(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GymForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have added a new Gym!')
            return redirect(reverse('add_gym'))
        else:
            messages.error(request, 'Your atempt to add a new Gym failed. Please make sure the form is valid.')
    else:
        form = GymForm()
        
    template = 'gyms/add_gym.html'
    context = {
        'form': form,
    }

    return render(request, template, context)