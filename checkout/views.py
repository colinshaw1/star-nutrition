from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from shoppingbag.contexts import bag_contents

import stripe

# Create your views here.
# checkour view


def checkout(request):
    # create stripe payment intent
    # public key
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # secret key
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # check submit method is post and submit request
    if request.method == 'POST':
        bag = request.session.get('bag', {})

        # get form data from dictionary
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        # if form is valid the order will get saved
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                # try catch
                try:
                    # get product id out of the bag
                    product = Product.objects.get(id=item_id)
                    # if value is integer it dosent have a size
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        # else has size will itterate through
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                # if product doesnt exist the error message will appear            
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            # add file info to the session and redierect to success page
            request.session['save_info'] = 'save-info' in request.POST
            # redirect to checout success pages
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            # if order form is invalid redirect and give error message
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
        # else return get request
    else:
        # get the bag from the session
        bag = request.session.get('bag', {})
        # if statment for logic around if bag is empty
        if not bag:
            messages.error(request, "Your bag is currently empty")
            return redirect(reverse('products'))

    # create new variable for stripe payments so the old one is not overridden
    current_bag = bag_contents(request)
    # getting the total key from the current bag
    total = current_bag['grand_total']
    # round the total for stripe
    stripe_total = round(total * 100)
    # setting secret key on stripe
    stripe.api_key = stripe_secret_key
    # createing the payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # creating the order form instance
    order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(
            request, 'Stripe public key is unavailable, please set before continuing')
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        # add stripe secret key
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # renders out the order form
    return render(request, template, context)

# checkout success view to let user know order is complete
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # check user wants ot save session
    save_info = request.session.get('save_info')
    # user oder number ot create order
    order = get_object_or_404(Order, order_number=order_number)
    # success message and order number noted
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    # delete users bag from the session
    if 'bag' in request.session:
        del request.session['bag']
    # setting the tempalte and context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    # return the template
    return render(request, template, context)