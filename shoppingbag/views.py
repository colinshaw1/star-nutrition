from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_bag(request):
    """ A view to return the bag content page"""

    return render(request, 'bag/bag.html')

# add in add to bag view
def add_to_bag(request, item_id):
    """Add quanity of a product to the shopping bag"""
    # get quanity and convert it to an integar as it is a string
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # set size to none
    size = None
    #if statement for product size in request . post it gets set to that
    if 'product_size' in request.POST:
        size = request.POST['size']
    # stores shopping bag in the sessions so it is not lost till the session is closed
    bag = request.session.get('bag', {})

    # if statment for sturcture of bag and check is size is been added
    if size: 
        # dictionary for size using key work item by sizefor multiple sizes
        if item_id in list(bag.keys()):
            # check two items of same id and size exist and set it equal to quantity
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    #else if item has no size run orginal         
    else:        
        # add item to bag or update the bag quanity if already in bag
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    # overwrite the variable if it doesnt exisit
    request.session['bag'] = bag
    return redirect(redirect_url)

# view update product quantity in the shopping bag
def update_bag(request, item_id):
    """Update the quantity of the items in the shopping bag"""
    # get quanity and convert it to an integar as it is a string
    quantity = int(request.POST.get('quantity'))
    # stores shopping bag in the sessions so it is not lost till the session is closed
    bag = request.session.get('bag', {})

    # update the bag quanity if already in bag
    if quantity > 0:
        bag[item_id] = quantity
    else:
        del bag[item_id]
    
    # overwrite the variable if it doesnt exisit
    request.session['bag'] = bag
    # redirect bag ot view bag url using the reverse
    return redirect(reverse('view_bag'))