from django.contrib import admin
#import model for products and categories
from .models import Product, Category

# class for extening django's built model admin feature
class ProductAdmin(admin.ModelAdmin):
    # tuple showing which fields to display
    list_display = (
        'sku',
        'name',
        'category',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    # tuple showing which fields to display
    list_display = (
        'friendly_name',
        'name',
    )
#registering the models for products and categories
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)