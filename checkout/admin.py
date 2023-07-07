from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

# class for order admin to generate administrion side
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    # read only fields so they can not be update and change the order
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)