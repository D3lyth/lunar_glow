from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from .models import Product, Category
from django.db.models.functions import Lower

from .forms import ProductForm

def all_products(request):
    """ A view of all products """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET.get('q', '')
            if not query:
                message.error(request, "You didn't enter any search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details  """

    product = get_object_or_404(Product, pk=product_id)

    # Get the search term from the query parameter
    search_term = request.GET.get('q', '')

    context = {
        'product': product,
        'search_term': search_term, #***********MIGHT NEED TO CHANGE THIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # 'current_category': categories, 
    }

    return render(request, 'products/product_detail.html', context)  


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)