from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

# allows admin users to add and edit line items in admin
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

# class for order admin to generate administrion side
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    # read only fields so they can not be update and change the order
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')
    # columns to show up in order list
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    
    # making sure orders will be ordered by date
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)