from django.shortcuts import render
from .models import Product

# Create your views here.

def products_view(request):
    """ A view to show all products, including sorting and search queries """

    # return products form databse
    products = Product.objects.all()

    context = {
        'products': products,
    }
    # return on products.html page
    return render(request, 'products/products.html', context)