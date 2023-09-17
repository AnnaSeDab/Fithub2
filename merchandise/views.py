from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category

# Create your views here.


def merchandise(request):
    """A view to return the page with all the merchandise, sorting and search"""

    products = Product.objects.all()
    
    context = {
        'products': products,
    }

    return render(request, 'merchandise/merchandise.html', context)


def product_detail(request, product_id):
    """A view to return the page with chosen product's details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'merchandise/product_detail.html', context)
