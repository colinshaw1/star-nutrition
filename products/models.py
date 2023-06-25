from django.db import models

# Create your models here.
#category model to seperate the products into categories
class Category(models.Model):
    #name of the catgory
    name = models.CharField(max_length=254)
    #friendly name of the category that will show up on the application
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name