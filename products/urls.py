from django.urls import path
from . import views

# view to call products   
urlpatterns = [
    path('', views.products_view, name='products'),
    # on product id return products details
    path('<product_id>', views.product_detail, name='product_detail'),
]