from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# makes all dictioanries avialble to all templeates on the app
def bag_contents(request):
    # setting bag items to an empty list
    bag_items = []
    # total set to 0
    total = 0
    # count set to 0
    product_count = 0
    # accessing the bag in session if it exists
    bag = request.session.get('bag', {})

    # for loop for each item and quanity in the bag to add to bag
    # add item_data to use all data not just quantity
    for item_id, item_data in bag.items():
        # if statment for code to be executed if it only has sizes.
        # if item is an integer it knows to use quantity
        if isinstance(item_data, int):
            # getting the product
            product = get_object_or_404(Product, pk=item_id)
            # add price and quantity to total
            total += item_data * product.price
            product_count += item_data
            # incremnts the product count by the quantity
            bag_items.append({
                # dictonary added to bag
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        # else it is a dictionary and it has to itterate accordingly through
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    # calculation for free shipping and adding on cost of shipping
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        # shows users if they spend a little more they will be able to get free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # returns a dictionary as context processer
    # makes context processor available in all templates
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,

    }

    return context