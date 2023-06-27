from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products_view(request):
    """ A view to show all products, including sorting and search queries """

    # return products form databse
    products = Product.objects.all()

    context = {
        'products': products,
    }
    #return on products.html page
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to single product details """

    # taking in project id and getting object 404
    product = get_object_or_40(product, pk=product_id)

    context = {
        'product': product,
    }
    # return on product details
    return render(request, 'products/product_details.html', context)