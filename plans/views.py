from django.shortcuts import render


def profile(request):
    """ Display Fitness plans. """

    template = 'plans/plans.html'
    context = {}

    return render(request, template, context)
