from django.db import models

# Create your models here.
#category model to seperate the products into categories
class Category(models.Model):
    #add meta class to change the spelling of categorys in admin to categories
    class Meta:
        verbose_name_plural = 'Categories'
    #name of the catgory to help make the name more code readable for views etc
    name = models.CharField(max_length=254)
    #friendly name of the category that will show up on the application
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # string to take in the category name and return the name
    def __str__(self):
        return self.name

     # model method to returnt he friendly name if needed
    def get_friendly_name(self):
        return self.friendly_name


#product model
class Product(models.Model):
    # foreign key to call upon the category model, if category is deleted so if any models use it null will be set
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # string method to return the product name same as category model
    def __str__(self):
        return self.name