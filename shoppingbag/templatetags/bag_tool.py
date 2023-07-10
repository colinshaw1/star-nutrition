from django import template

# taken from the django documention
register = template.Library()

#registers the filter as a template
@register.filter(name="calc_subtotal")
# function that takes in a price and parm and returns the product
def calc_subtotal(price, quantity):
    return price * quantity