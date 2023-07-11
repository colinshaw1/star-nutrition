from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms  import OrderForm

# Create your views here.
# checkout view
def checkout(request):
    # get the bag from the session
    bag = request.session.get('bag', {})
    # if statment for logic around if bag is empty
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(reverse('products'))

    # creating the order form instance
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        # add stripe secret key
        'stripe_public_key': 'pk_test_51M1CYYGLT9eFji1UAXkz1tcBoXIzozeKbxP3j2Tf31pRfj8qD2bcczgQjwfMCQEC3el0XZYIY4CBY7oaRKvaXp9w00XkO37pJh',
        'client_secret': 'test client secret',
    }

    # renders out the order form
    return render(request, template, context)