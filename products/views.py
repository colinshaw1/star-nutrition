from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def products_view(request):
    """ A view to show all products, including sorting and search queries """

    # return products form databse
    products = Product.objects.all()
    #stops an error wehn loading products page without a search term
    query = None

    # method taken from course content
    # checking if requests. GET exists
    if request.GET:
        # if q is in request.GET equal query
        if 'q' in request.GET:
            query = request.GET['q']
            # if q is in request.GET equal error message
            if not query:
                messages.error(request, "Please check your search query and try agian?")
                return redirect(reversal('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # passing to filter message to filter products
            products = products.filter(queries)

    context = {
        'products': products,
        # query added to context
        'search_term' : query,
    }
    #return on products.html page
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to single product details """

    # taking in project id and getting object 404
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    # return on product details
    return render(request, 'products/product_detail.html', context)