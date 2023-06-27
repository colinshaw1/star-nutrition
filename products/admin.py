from django.contrib import admin
#import model for products and categories
from .models import Product, Category

# Register your models here.
#registering the models for products and categories
admin.site.register(Product)
admin.site.register(Category)