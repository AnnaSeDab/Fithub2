from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from merchandise.models import Product
from profiles.models import UserProfile

# Create your views here.


def view_bag(request):
    """A view to return the bag content page"""
    return render(request, 'bag/bag.html')


def adjust_bag(request, item_id):
    """ Adjust a quantity of the specified product in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed size {size.upper()} {product.name} from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # Check if user logged in and does not have a fitness plan already
    if product.is_plan == True:
        if request.user.is_authenticated:
            profile = get_object_or_404(UserProfile, user=request.user)
            if profile.fitness_plan:
                messages.warning(
                    request, f"You aready purchased a fitness plan. Please contact us at admin@emailaddress.com if you'd like to discuss changing your plan")
            else:
                if item_id in list(bag.keys()):
                    messages.warning(
                        request, f'You cannot buy two Fitness Plans at the same time')
                else:
                    bag[item_id] = quantity
                    messages.success(
                        request, f'Added {product.name} to your bag')
        else:
            messages.warning(
                request, f'You have to be logged in to purchase a fitness plan')
    else:
        if size:
            if item_id in list(bag.keys()):
                if size in bag[item_id]['items_by_size'].keys():
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(
                        request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
                else:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(
                        request, f'Added size {size.upper()} {product.name} to your bag')
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
                messages.success(
                    request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            if item_id in list(bag.keys()):
                bag[item_id] += quantity
                messages.success(
                    request, f'Updated {product.name} quantity to {bag[item_id]}')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
